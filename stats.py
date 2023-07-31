from dbpedia import endpoints
from query import query_endpoint


endpoint_versions = {"totalVersions": "0", "endpoints": []}


for endpoint, query in endpoints.items():
    db = query_endpoint(endpoint, query)
    endpoint_versions["endpoints"].append(endpoint)
    version_count = int(db["Versions"]["value"])
    endpoint_versions["totalVersions"] = f"{version_count + int(endpoint_versions['totalVersions'])}" 


print(endpoint_versions)
