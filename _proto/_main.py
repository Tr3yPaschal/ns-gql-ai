from proto.geocode_hotelSummaryOptions import execute_query

def main():
    # Collect user input for the location
    location = input("Enter the location (e.g., dallas,texas,usa): ")
    
    try:
        # Execute the GraphQL query with the provided location
        response_data = execute_query(address=location)

        # Print the response data
        print("Query successful!")
        print(response_data)
    except Exception as e:
        # Print any errors that occur during the query
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
