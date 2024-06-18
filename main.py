import json 
from common.query import Query
from common.query_variables import QueryVariables
from common.execute_query import execute_query
from common.terminal_colors import TerminalColors
from common.localRec import LocalRec

def main():
    
    #Hotel Details
    query_name = 'hotel'
    operation_name = 'hotel'
    variables = QueryVariables(
        ctyhocn= "LAXAVCI",
        language="en-US"
    )

    hotel = execute_query(query_name,operation_name, variables) 

    print("\n")
    print(TerminalColors.color_text("Hotel Policy", TerminalColors.GREEN))
    # Format the JSON response and save it to a file
    formatted_json = json.dumps(hotel.data, indent=4)
    with open('example_data/hotel_details.json', 'w') as json_file:
        json_file.write(formatted_json)
        print("Hotel policy saved to hotel_policy.json")
        

if __name__ == "__main__":
    main()
