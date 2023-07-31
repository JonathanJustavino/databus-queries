from SPARQLWrapper import SPARQLWrapper, JSON


def query_endpoint(endpoint, query):
    sparql = SPARQLWrapper(
        endpoint
    )

    sparql.setReturnFormat(JSON)

    try:
        sparql.setQuery(query)
        response = sparql.queryAndConvert()

        for result in response["results"]["bindings"]:
            return result

    except Exception as error:
        print(error)
