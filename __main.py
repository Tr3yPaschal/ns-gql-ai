import os
from common.query import Query
from common.query_variables import QueryVariables
#from common.query_response import QueryResponse
from common.execute_query import execute_query

def load_query(query_file):
    with open(query_file, 'r') as file:
        return file.read()

def main():
    query_dir = 'queries'
    query_files = [
        'geocodeHotelSummaryOptions.gql',
        'hotel.gql'
    ]

    for query_file in query_files:
        query_path = os.path.join(query_dir, query_file)
        query_name = os.path.splitext(query_file)[0]

        # Load the query template
        query_string = load_query(query_path)

        # Define variables for the query
        variables = QueryVariables(
            address="Dallas",
            language="en",
            queryLimit=150,
            distanceUnit="mi",
            placeId=None,
            sessionToken="your-session-token"
        )

        # Instantiate Query object
        query_obj = Query(query_name, query_string, variables.get_variables())

        # Execute the query
        response = execute_query(query_obj)

        # Process the response
        process_response(response, query_name)

def process_response(response, query_name):
    if response.status_code == 200:
        print(f"Result of '{query_name}' query:")
        print(response.data)
    else:
        print(f"Query '{query_name}' failed with status code {response.status_code}")

if __name__ == "__main__":
    main()
