from common.query import Query
from common.query_variables import QueryVariables
from common.execute_query import execute_query
from common.terminal_colors import TerminalColors
from common.hms_api import HMS_API

def main():
    
# Define your constants

    base_url = "https://hmsstg.hiltonapi.com/hms/v1/"
    method_signature = "core/localRecommendations"
    querystring = {"ctyhocn": "DCAOTHF"}
    secret_key = "52tBVaCe"
    app_key = "hhonors"
    device_id = "a235c98737c63559"

    # Create an instance of HMS_API
    api = HMS_API(base_url, method_signature, querystring, secret_key, app_key, device_id)

    # Example usage of set_json_attribute method
    config_name = "example_config"
    version = "1.0"
    attribute_name = "example_attribute"
    attribute_json = {"key": "value"}

    response = api.set_json_attribute(config_name, version, attribute_name, attribute_json)

    # Handle the response
    if response.has_error:
        print(f"Error: {response.response_value}")
    else:
        print(f"Success: {response.response_value}")
    
    """ query_name = 'geocodeHotels'
    operation_name = 'geocodeHotels'
    variables = QueryVariables(
            address="Dallas",
            language="en",
            distanceUnit="mi",
            placeId=None,
            sessionToken="your-session-token"
        ) """

    # Execute the query
    """ hotel_list = execute_query(query_name, operation_name, variables)

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
        print("\n") """

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
