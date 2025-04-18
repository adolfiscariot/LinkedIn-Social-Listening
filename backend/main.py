#This is the main module

import json
import psycopg
import logging
from typing import Dict, Any
from config import logging_config
from services.icp_scoring import icp_scoring
from flask import Flask, jsonify, Response, stream_with_context
from flask_cors import CORS

#create a flask app
app = Flask(__name__)
CORS(app)

#initialize logging configs
logging_config.configure_logging()

#create module level logger
logger = logging.getLogger(__name__)
    
#minimum score for a lead to become qualified
MIN_SCORE = 0

#endpoint to retrieve qualified leads based on icp scoring.
@app.route('/lead-data', methods=['GET'])
def lead_data() -> Dict[str, Any]:

    try:
        logger.info("Starting process of fetching lead data...")
        
        #run icp scoring. it will call get authors which will call search posts
        lead_data = icp_scoring(min_score=MIN_SCORE)

        logger.info(
           "Successfully retrieved %d qualified leads", len(lead_data),
           extra={"metrics": {
               "Qualified Leads": len(lead_data)
           }} 
        )

        return jsonify({
            "status": "success",
            "count": len(lead_data),
            "data": lead_data
        })

    except Exception as e:
        logging.error(
            "Lead data could not be retrieved",
            exc_info=True,
            extra={"error_details": str(e)}
        )
        return jsonify({
            "status": "error", 
            "message": "Failed to retrieve lead data",
        }), 500

@app.route('/stream-leads', methods=['GET'])
def stream_leads():
    def generate():
        try:
            with psycopg.connect(conninfo="host=localhost dbname=sl port=5432 user=postgres password=markothengo99") as conn:
                with conn.cursor() as cur:
                    for scored_lead in icp_scoring(min_score=MIN_SCORE):
                        if "error" in scored_lead:
                            yield f"data: {json.dumps(scored_lead)}\n\n"
                        else:
                            # Extract data from the scored lead
                            author = scored_lead.get('author', {})
                            company_name = author.get('company', '')
                            company_industry = author.get('company_industry', '')
                            company_location = author.get('location', '')
                            employee_size = author.get('employee_count', '')
                            name = author.get('name', '')
                            job_title = author.get('job_title', '')
                            
                            # Store in DB
                            try:
                                cur.execute(
                                    "INSERT INTO companies (name, industry, location, employee_count) VALUES (%s, %s, %s, %s) RETURNING company_id",
                                    (company_name, company_industry, company_location, employee_size)
                                )
                                company_id = cur.fetchone()[0]
                                cur.execute(
                                    "INSERT INTO authors (name, title, company_id) VALUES (%s, %s, %s)",
                                    (name, job_title, company_id)
                                )
                                logger.info("Data inserted into Authors!")
                            except Exception as e:
                                logger.error(f"Database error: {str(e)}")
                            
                            yield f"data: {json.dumps(scored_lead)}\n\n"
                            
                conn.commit()
        except Exception as e:
            logger.error(f"Streaming error: {str(e)}")
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
    
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == "__main__":
    #run the flask app
    logger.info("Starting flask app...")
    app.run(debug=True)