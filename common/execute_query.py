import os
import requests
from common.query_response import QueryResponse

def execute_query(query_name, operation_name, variables):
    # Load the query template
    query_path = os.path.join('gql_queries', f"{query_name}.gql")
    with open(query_path, 'r') as file:
        query_string = file.read()

    # Define the GraphQL endpoint and headers
    url = 'https://m.stg.hilton.io/graphql/customer'
    headers = {'Content-Type': 'application/json'}

    # Make the request
    response = requests.post(
        url,
        headers=headers,
        json={'operationName': operation_name, 'query': query_string, 'variables': variables.get_variables()}
    )

    # Check for a successful response
    if response.status_code == 200:
        return QueryResponse(response.json(), response.status_code)
    else:
        return QueryResponse(response.text, response.status_code)
