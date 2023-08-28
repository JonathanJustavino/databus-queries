import os
import re
import csv
import json
from textwrap import fill
from SPARQLWrapper import SPARQLWrapper, JSON, CSV


def save_result(result, filename="dbversion.json", fcsv="dbversion.csv"):
    basepath = os.getcwd()
    save_csv = os.path.join(basepath, fcsv)
    save_json = os.path.join(basepath, filename)
    json_obj = json.dumps(result, indent=4)



    # with open(save_json, "w") as output:
    #     output.write(json_obj)

    # with open(save_csv, "w") as file:
    #     csv_writer = csv.writer(file)
    #     for row in result:
    #         print(row)
    return result


def query_endpoint(endpoint, query, query_path):
    sparql = SPARQLWrapper(
        endpoint
    )

    # sparql.setReturnFormat(JSON)
    sparql.setReturnFormat(CSV)

    try:
        sparql.setQuery(query)
        response = sparql.queryAndConvert()
        data = response.decode('utf-8').splitlines()

        basepath = os.getcwd()
        name = re.sub("http[s]://", "", endpoint)
        name = re.sub("\/", "-", name)
        filepath = os.path.join(basepath, f"{query_path}-{name}.csv")

        with open(filepath, 'w+') as csv_file:
            writer = csv.writer(csv_file, delimiter='\n')
            for line in data:
                writer.writerow(re.split('\n', line))


        # print(response)
        # response = save_result(response)
        # print(response)
        # print(response)
        return response

        # for result in response["results"]["bindings"]:
        #     return result

    except Exception as error:
        print(error)
