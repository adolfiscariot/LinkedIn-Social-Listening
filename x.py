from linkedin_api import Linkedin
from ratelimit import sleep_and_retry, limits
import json

# api = Linkedin("markmathengeequity@gmail.com", "sociallistening")
# rate_limit = 1
# #Search for posts based on keywords
# params = {"keywords":"call center"}

# @sleep_and_retry
# @limits(calls=1, period=rate_limit)
# def search_posts(params: dict) -> list:
#     print("Search starting...")
#     search = api.search(params, limit = 3)
#     print("Search ended!")
#     time.sleep(rate_limit)
#     print(search)
#     return search 

# search_posts(params)

x = {'template': 'CONTENT_B', 'actorNavigationContext': {'_type': 'com.linkedin.voyager.dash.search.NavigationContext', 'openExternally': False, '_recipeType': 'com.linkedin.55ee9afd4182671fe7e271f615659525', 'url': 'https://www.linkedin.com/in/ACoAAAFnJGkBOSn-Lvrj-P-ZiP6e-jnvD8UQceI?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAFnJGkBOSn-Lvrj-P-ZiP6e-jnvD8UQceI'}, 'trackingUrn': 'urn:li:activity:7294761543949262848', 'controlName': 
None, 'interstitialComponent': None, 'primaryActions': [], 'entityCustomTrackingInfo': None, 'title': {'textDirection': 'FIRST_STRONG', '_type': 'com.linkedin.voyager.dash.common.text.TextViewModel', 'text': 'Krishani Dela', 'attributesV2': [], '_recipeType': 'com.linkedin.6a224ca38654a84754a1eb3e97c0f846', 'accessibilityTextAttributesV2': [], 'accessibilityText': 'View Krishani Dela’s profile'}, 'overflowActions': [], 'searchActionType': None, 'actorInsights': [], 'insightsResolutionResults': [{'jobPostingInsight': None, 'relationshipsInsight': None, 'serviceProviderRatingInsight': None, 'simpleInsight': None, 'jobPostingFooterInsight': None, 'socialActivityCountsInsight': None, 'labelsInsight': None}], 'badgeIcon': None, 'entityUrn': 'urn:li:fsd_entityResultViewModel:(urn:li:activity:7294761543949262848,SEARCH_SRP,DEFAULT)', 'showAdditionalCluster': False, 'ringStatus': None, 'primarySubtitle': {'textDirection': 'USER_LOCALE', '_type': 'com.linkedin.voyager.dash.common.text.TextViewModel', 'text': 'Recruiter / Human Resource Business Partner / Certified Job Analyst / HR Generalist / Online Trainer', 'attributesV2': [], '_recipeType': 'com.linkedin.6a224ca38654a84754a1eb3e97c0f846', 'accessibilityTextAttributesV2': [], 'accessibilityText': None}, 'badgeText': {'textDirection': 'USER_LOCALE', '_type': 'com.linkedin.voyager.dash.common.text.TextViewModel', 'text': '• 3rd+', 'attributesV2': [], '_recipeType': 'com.linkedin.6a224ca38654a84754a1eb3e97c0f846', 'accessibilityTextAttributesV2': [], 'accessibilityText': None}, 'trackingId': 'mMg0RM88S0uRjAXsXjrZtw==', 'summary': {'textDirection': 'USER_LOCALE', '_type': 'com.linkedin.voyager.dash.common.text.TextViewModel', 'text': 'We’re #hiring Call Center Executives. Apply today.', 'attributesV2': [], '_recipeType': 'com.linkedin.6a224ca38654a84754a1eb3e97c0f846', 'accessibilityTextAttributesV2': [], 'accessibilityText': None}, 'actorNavigationUrl': 'https://www.linkedin.com/in/ACoAAAFnJGkBOSn-Lvrj-P-ZiP6e-jnvD8UQceI?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAFnJGkBOSn-Lvrj-P-ZiP6e-jnvD8UQceI', 'addEntityToSearchHistory': False, 'image': {'_type': 'com.linkedin.voyager.dash.common.image.ImageViewModel', 'attributes': [{'scalingType': None, '_type': 'com.linkedin.voyager.dash.common.image.ImageAttribute', 'detailData': {'profilePictureWithoutFrame': None, 'profilePictureWithRingStatus': None, 'companyLogo': None, 'icon': None, 'systemImage': None, 'nonEntityGroupLogo': None, 'vectorImage': None, 'nonEntityProfessionalEventLogo': None, 'profilePicture': None, 'imageUrl': None, 'professionalEventLogo': None, 'nonEntityCompanyLogo': None, 'nonEntitySchoolLogo': None, 'groupLogo': None, 'schoolLogo': None, 'ghostImage': None, 'nonEntityProfilePicture': {'_type': 'com.linkedin.voyager.dash.common.image.NonEntityProfilePicture', 'ringStatus': None, '_recipeType': 'com.linkedin.4b009c1d6ea192a94bda77fb9ace3a7d', 'vectorImage': {'_type': 'com.linkedin.common.VectorImage', 'attribution': None, '_recipeType': 'com.linkedin.28db8575bcf1c65bdc4bc15948d50ee9', 'digitalmediaAsset': None, 'artifacts': [{'width': 100, '_type': 'com.linkedin.common.VectorArtifact', '_recipeType': 'com.linkedin.f0f435b4425ee2990eba8f0a4d614944', 'fileIdentifyingUrlPathSegment': 'https://media.licdn.com/dms/image/v2/D5603AQGEhxmpWdvO8w/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1713338458854?e=1744848000&v=beta&t=mgf18qDBL4x2K3ap0AHYDQjha7azh0TiNQlgD40nTx8', 'expiresAt': 1744848000000, 'height': 100}], 'rootUrl': ''}, 'profile': {'_recipeType': 'com.linkedin.e0372afc4a18480b00ca7e4906904fd7', '_type': 'com.linkedin.voyager.dash.identity.profile.Profile', 'entityUrn': 'urn:li:fsd_profile:ACoAAAFnJGkBOSn-Lvrj-P-ZiP6e-jnvD8UQceI'}}}, 'tintColor': None, '_recipeType': 'com.linkedin.eb94fbb1518f790c4545aafdf571c64e', 'tapTargets': [], 'displayAspectRatio': None}], 'actionTarget': None, '_recipeType': 'com.linkedin.fe5b8a3ac5a4a165c17f53b7eae4209b', 'accessibilityTextAttributes': [], 'totalCount': None, 'accessibilityText': 'Krishani Dela'}, 'lazyLoadedActions': {'_recipeType': 'com.linkedin.92ece182782ae4412e712925cd97f9fe', 
'_type': 'com.linkedin.voyager.dash.search.LazyLoadedActions', 'entityUrn': 'urn:li:fsd_lazyLoadedActions:(urn:li:activity:7294761543949262848,CONTENT,SEARCH_SRP)'}, 'secondarySubtitle': {'textDirection': 'USER_LOCALE', '_type': 'com.linkedin.voyager.dash.common.text.TextViewModel', 'text': '15h •  ', 'attributesV2': [{'start': 6, 'length': 1, '_type': 'com.linkedin.voyager.dash.common.text.TextAttribute', 'detailData': {'jobPostingName': None, 'hyperlink': None, 'profileFamiliarName': None, 'color': None, 'companyName': None, 'icon': 'IC_GLOBE_16DP', 'epoch': None, 'systemImage': None, 'textLink': None, 'listItemStyle': None, 'groupName': None, 
'hyperlinkOpenExternally': None, 'listStyle': None, 'profileFullName': None, 'stringFieldReference': None, 'learningCourseName': None, 'profileMention': None, 'style': None, 'schoolName': None, 'hashtag': None}, '_recipeType': 'com.linkedin.b8a09c2c7547138a1c3aebdda8a94e12'}], '_recipeType': 'com.linkedin.6a224ca38654a84754a1eb3e97c0f846', 'accessibilityTextAttributesV2': [], 'accessibilityText': None}, '_type': 'com.linkedin.voyager.dash.search.EntityResultViewModel', 'entityEmbeddedObject': {'summary': None, 'image': {'_type': 'com.linkedin.voyager.dash.common.image.ImageViewModel', 'attributes': [{'scalingType': 'ASPECT_FILL', '_type': 'com.linkedin.voyager.dash.common.image.ImageAttribute', 'detailData': {'profilePictureWithoutFrame': None, 'profilePictureWithRingStatus': None, 'companyLogo': None, 'icon': None, 'systemImage': None, 'nonEntityGroupLogo': None, 'vectorImage': None, 'nonEntityProfessionalEventLogo': None, 'profilePicture': None, 'imageUrl': None, 'professionalEventLogo': None, 'nonEntityCompanyLogo': {'_type': 'com.linkedin.voyager.dash.common.image.NonEntityCompanyLogo', 'company': {'_recipeType': 'com.linkedin.2c2374bef3eaba3e079b4a11e2f7bea8', '_type': 'com.linkedin.voyager.dash.organization.Company', 'entityUrn': 'urn:li:fsd_company:14623244'}, '_recipeType': 'com.linkedin.3be27b5a0eb7edd91e98b14c0290096c', 'vectorImage': {'_type': 'com.linkedin.common.VectorImage', 'attribution': None, '_recipeType': 'com.linkedin.28db8575bcf1c65bdc4bc15948d50ee9', 'digitalmediaAsset': None, 'artifacts': [{'width': 200, '_type': 'com.linkedin.common.VectorArtifact', '_recipeType': 'com.linkedin.f0f435b4425ee2990eba8f0a4d614944', 'fileIdentifyingUrlPathSegment': '200_200/company-logo_200_200/0/1630646931271?e=1747267200&v=beta&t=oaxqjqpGKJxvgaO-g_rJhi57FKeoPSyMI5ykVSkqcZQ', 'expiresAt': 1747267200000, 'height': 200}, {'width': 100, '_type': 'com.linkedin.common.VectorArtifact', '_recipeType': 'com.linkedin.f0f435b4425ee2990eba8f0a4d614944', 'fileIdentifyingUrlPathSegment': '100_100/company-logo_100_100/0/1630646931271?e=1747267200&v=beta&t=Zjm1Xfxwg3C0mSesrOktYbZj--PYaqPJw-tuOGqSyOg', 'expiresAt': 1747267200000, 'height': 100}, {'width': 400, '_type': 'com.linkedin.common.VectorArtifact', '_recipeType': 'com.linkedin.f0f435b4425ee2990eba8f0a4d614944', 'fileIdentifyingUrlPathSegment': '400_400/company-logo_400_400/0/1630646931271?e=1747267200&v=beta&t=4cyDGtsbLQGF34X2GRSjOmJX6R2NJ764wf-C4XTsg1Y', 'expiresAt': 1747267200000, 'height': 400}], 'rootUrl': 'https://media.licdn.com/dms/image/v2/C560BAQGplG-OJazYng/company-logo_'}}, 'nonEntitySchoolLogo': None, 'groupLogo': None, 'schoolLogo': None, 'ghostImage': None, 'nonEntityProfilePicture': None}, 'tintColor': None, '_recipeType': 'com.linkedin.eb94fbb1518f790c4545aafdf571c64e', 'tapTargets': [], 'displayAspectRatio': None}], 'actionTarget': None, '_recipeType': 'com.linkedin.fe5b8a3ac5a4a165c17f53b7eae4209b', 'accessibilityTextAttributes': [], 'totalCount': None, 'accessibilityText': 'Image preview'}, 'headerThumbnail': None, 'secondarySubtitle': None, 'trackingUrn': None, '_type': 'com.linkedin.voyager.dash.search.EntityEmbeddedObject', 'primaryActions': [], 'showPlayButton': False, 'title': {'textDirection': 'FIRST_STRONG', '_type': 'com.linkedin.voyager.dash.common.text.TextViewModel', 'text': 'Call Center Executive', 'attributesV2': [], '_recipeType': 'com.linkedin.6a224ca38654a84754a1eb3e97c0f846', 'accessibilityTextAttributesV2': [], 'accessibilityText': None}, '_recipeType': 'com.linkedin.bd93318ac5710b71fba68ebb50fd5bfd', 'renderStyle': 'DEFAULT_CONTENT', 'primarySubtitle': {'textDirection': 'USER_LOCALE', '_type': 'com.linkedin.voyager.dash.common.text.TextViewModel', 'text': 'Job by Abans Group Sri Lanka', 'attributesV2': [], '_recipeType': 'com.linkedin.6a224ca38654a84754a1eb3e97c0f846', 'accessibilityTextAttributesV2': [], 'accessibilityText': None}, 'headerTitle': None}, 'navigationUrl': 'https://www.linkedin.com/feed/update/urn:li:activity:7294761543949262848?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7294761543949262848%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29', 'unreadIndicatorDetails': None, '_recipeType': 'com.linkedin.cf4b25c18907ea8eafe915c8bfa24109', 'target': {'updateV2Urn': 'urn:li:fs_updateV2:(urn:li:activity:7294761543949262848,BLENDED_SEARCH_FEED,EMPTY,DEFAULT,false)', 'profile': None}, 'actorTrackingUrn': 'urn:li:member:23536745', 'navigationContext': {'_type': 'com.linkedin.voyager.dash.search.NavigationContext', 'openExternally': False, '_recipeType': 'com.linkedin.55ee9afd4182671fe7e271f615659525', 'url': 'https://www.linkedin.com/feed/update/urn:li:activity:7294761543949262848?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7294761543949262848%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29'}}
print(json.dumps(x, indent = 4))