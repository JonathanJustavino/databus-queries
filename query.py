from SPARQLWrapper import SPARQLWrapper, JSON

endpoint = "https://dev.databus.dbpedia.org/sparql"

sparql = SPARQLWrapper(
    endpoint
)

sparql.setReturnFormat(JSON)

column_name = "Versions"

db_query = f"""
PREFIX databus: <https://dataid.dbpedia.org/databus#>
SELECT COUNT(?s) as ?{column_name} {{
?s a databus:Version
}}
"""

try:
    sparql.setQuery(db_query)
    response = sparql.queryAndConvert()

    for result in response["results"]["bindings"]:
        print(result)
    # print(results["results"]["callret-0"].value)
except Exception as error:
    print(error)