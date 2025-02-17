import re
locations = {"Pakistan", "India", "Kenya"}
lis = {"manager", "boss", "ceo"}
info = "Asadullah Mughal - Human Resources Manager | MBA in Human Resources - The Auctus - Karachi Division, Sindh, Pakistan - 1001 to 4000"
parts = info.split(" - ")
name = parts[0]
title = parts[1]
company = parts[2]
location = parts[3]
employees = parts[4]

person = {
        "Name": name,
        "Title":title,
        "Company":company,
        "Location":location,
        "Employees":employees
        }

new_person = employees.strip()
pattern = r"(\d+)$"

result = re.search(pattern, new_person)

if result and any(word.lower() in title.lower() for word in lis) and any(word.lower() in location.lower() for word in locations):
    print("yesssssssssirrrrrrrrrrrr!!")
