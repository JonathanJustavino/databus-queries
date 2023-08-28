import os
import json
import pandas as pd
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


def create_results_json(data, filename="dbversions.json"):
    save_json = os.path.join(basepath, filename)
    save_csv = os.path.join(basepath, "dbversions2.csv")
    # output = json.dumps(data, indent=4)
    # with open(result_json, "w") as file:
    #     file.write(output)

    json_obj = json.dumps(data, indent=4)
    print("pree")

    with open(save_json, "w") as output:
        output.write(json_obj)
        df = pd.read_json(json_obj)
        df.to_csv(save_csv, sep=',', encoding='utf-8', index=False)


endpoints = get_endpoints(endpoints_path)
query = load_sparql_query(stats_query_path)


def main():
    endpoint_results = {}

    for endpoint in endpoints:
        db = query_endpoint(endpoint, query, stats_query_path)
        endpoint_results[endpoint] = db
        print(db)
        # version_count = db["results"]["bindings"][0]["Version"]["value"]
        # endpoint_versions[endpoint] = version_count
        # endpoint_versions["totalVersions"] = f"{int(version_count) + int(endpoint_versions['totalVersions'])}" 
    
    # create_results_json(endpoint_results)
    return endpoint_versions


if __name__ == '__main__':
    versions = main()
    print(versions)
