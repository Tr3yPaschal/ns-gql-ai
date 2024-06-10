from common.query import Query
from common.query_variables import QueryVariables
from common.execute_query import execute_query
from common.terminal_colors import TerminalColors

def main():
    
    query_name = 'geocodeHotels'
    operation_name = 'geocodeHotels'
    variables = QueryVariables(
            address="Dallas",
            language="en",
            distanceUnit="mi",
            placeId=None,
            sessionToken="your-session-token"
        )

    # Execute the query
    hotel_list = execute_query(query_name, operation_name, variables)

    # Iterate over the hotel data
    for hotel in hotel_list.data['data']['geocode']['ctyhocnList']['hotelList']:
        print(TerminalColors.color_text(hotel['ctyhocn'], TerminalColors.GREEN))
        query_name = 'hotel'
        operation_name = 'hotel'
        variables = QueryVariables(
            ctyhocn=hotel['ctyhocn'],
            language="en-US"
        )
        hotel_details = execute_query(query_name,operation_name, variables) 
        print(TerminalColors.color_text("Hotel Details", TerminalColors.GREEN))
        print(hotel_details.data)
        print("\n")

    # hotelSumarryOptions
    """query_name = 'geocodeHotelSummaryOptions'
    operation_name = 'geocodeHotelSummaryOptions'
    variables = QueryVariables(
        address="Dallas",
        language="en",
        queryLimit=150,
        distanceUnit="mi",
        placeId=None,
        sessionToken="your-session-token"
    )

    # Execute the query
    hotel_list = execute_query(query_name,operation_name, variables)

    print(TerminalColors.color_text("Hotel Results", TerminalColors.GREEN))
    print(hotel_list.data)"""

    


    #hotelSumarryOptionsAmenities
    """query_name = 'hotelSummaryOptions_amenities'
    operation_name = 'hotelSummaryOptions'
    variables = QueryVariables(
        ctyhocn= ["LAXAVCI","DCAOTHF"],
        language="en-US"
    )

    hotel_amenitites = execute_query(query_name,operation_name, variables) 

    print("/n")
    print(TerminalColors.color_text("Hotel Amenities", TerminalColors.GREEN))
    print(hotel_amenitites.data)"""

    #hotelPolicy
    """query_name = 'hotelPolicy'
    operation_name = 'hotelPolicy'
    variables = QueryVariables(
        ctyhocn= "LAXAVCI",
        language="en-US"
    )

    hotel_policy = execute_query(query_name,operation_name, variables) 

    print("\n")
    print(TerminalColors.color_text("Hotel Policy", TerminalColors.GREEN))
    print(hotel_policy.data)"""

if __name__ == "__main__":
    main()
