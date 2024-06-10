from common.query import Query
from common.query_variables import QueryVariables
from common.execute_query import execute_query

def main():
    # Define the query and variables
    query_name = 'geocodeHotelSummaryOptions'
    variables = QueryVariables(
        address="Dallas",
        language="en",
        queryLimit=150,
        distanceUnit="mi",
        placeId=None,
        sessionToken="your-session-token"
    )

    # Execute the query
    hotel_list = execute_query(query_name, variables)

    # Print the response data
    print(hotel_list.data)

    query_name = 'hotel'
    variables = QueryVariables(
        ctyhocn="LAXAVCI",
        language="en-US"
    )

    hotel_details = execute_query(query_name, variables)

    print("/n")

    print(hotel_details.data)

if __name__ == "__main__":
    main()
