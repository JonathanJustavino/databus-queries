db_endpoint = "https://databus.dbpedia.org/sparql"
dev_db_endpoint = "https://dev.databus.dbpedia.org/sparql"

column_name = "Versions"

db_query = f"""
PREFIX databus: <https://dataid.dbpedia.org/databus#>
SELECT COUNT(?s) as ?{column_name} {{
?s a databus:Version
}}
"""

dev_db_query = f"""
PREFIX databus: <https://dataid.dbpedia.org/databus#>
SELECT COUNT(?s) as ?{column_name} {{
?s a databus:Version
}}
"""

endpoints = {
    db_endpoint: db_query,
    dev_db_endpoint: dev_db_query,
}
