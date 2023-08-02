import os
from query import query_endpoint


basepath = os.getcwd()

endpoints_file = "databuses.txt"
endpoints_path = os.path.join(basepath, endpoints_file)

stats_query_file = "stats-query.rq"
stats_query_path = os.path.join(basepath, stats_query_file)

endpoint_versions = {"totalVersions": "0"}


def get_endpoints(endpoints_path):
    endpoints = []

    with open(endpoints_path, mode="r") as file:
        for endpoint in file:
            endpoints.append(endpoint.strip())
    return endpoints


def load_sparql_query(query_path):
    with open(query_path, mode="r") as file:
        return file.read()


endpoints = get_endpoints(endpoints_path)
query = load_sparql_query(stats_query_path)


def main():
    for endpoint in endpoints:
        db = query_endpoint(endpoint, query)
        version_count = db["Version"]["value"]
        endpoint_versions[endpoint] = version_count
        endpoint_versions["totalVersions"] = f"{int(version_count) + int(endpoint_versions['totalVersions'])}" 
    return endpoint_versions


if __name__ == '__main__':
    versions = main()
    print(versions)
