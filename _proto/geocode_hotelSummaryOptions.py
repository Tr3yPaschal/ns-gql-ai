import requests

def execute_query(address, language="en", query_limit=150, distance_unit="mi", place_id=None, session_token="your-session-token"):
    # Define the GraphQL endpoint and headers
    url = 'https://m.stg.hilton.io/graphql/customer?operationName=geocode_hotelSummaryOptions'
    headers = {'Content-Type': 'application/json'}

    # Define the GraphQL query
    query = """
    query geocodeHotelSummaryOptions($address: String, $distanceUnit: HotelDistanceUnit, $language: String!, $placeId: String, $queryLimit: Int!, $sessionToken: String) {
      geocode(
        language: $language
        address: $address
        placeId: $placeId
        sessionToken: $sessionToken
      ) {
        match {
          id
          address {
            city
            country
            state
          }
          name
          type
          geometry {
            location {
              latitude
              longitude
            }
            bounds {
              northeast {
                latitude
                longitude
              }
              southwest {
                latitude
                longitude
              }
            }
          }
        }
        hotelSummaryOptions(distanceUnit: $distanceUnit, sortBy: distance) {
          bounds {
            northeast {
              latitude
              longitude
            }
            southwest {
              latitude
              longitude
            }
          }
          amenities {
            id
            name
            hint
          }
          amenityCategories {
            name
            id
            amenityIds
          }
          brands {
            code
            name
          }
          hotels(first: $queryLimit) {
            _id: ctyhocn
            amenityIds
            brandCode
            ctyhocn
            distance
            distanceFmt
            facilityOverview {
              allowAdultsOnly
            }
            name
            display {
              open
              openDate
              preOpenMsg
              resEnabled
              resEnabledDate
            }
            contactInfo {
              phoneNumber
            }
            address {
              addressLine1
              city
              country
              state
            }
            localization {
              coordinate {
                latitude
                longitude
              }
            }
            images {
              master(variant: searchPropertyImageThumbnail) {
                altText
                variants {
                  size
                  url
                }
              }
            }
            tripAdvisorLocationSummary {
              numReviews
              rating
              ratingFmt(decimal: 1)
              ratingImageUrl
              reviews {
                id
                rating
                helpfulVotes
                ratingImageUrl
                text
                travelDate
                user {
                  username
                }
                title
              }
            }
            leadRate {
              hhonors {
                max {
                  rateAmount
                  rateAmountFmt
                  dailyRmPointsRate
                  dailyRmPointsRateFmt
                  ratePlan {
                    ratePlanCode
                  }
                }
                min {
                  rateAmount
                  rateAmountFmt
                  dailyRmPointsRate
                  dailyRmPointsRateFmt
                  ratePlan {
                    ratePlanCode
                  }
                }
              }
            }
          }
        }
        ctyhocnList: hotelSummaryOptions(distanceUnit: $distanceUnit, sortBy: distance) {
          hotelList: hotels(first: 150) {
            ctyhocn
          }
        }
      }
    }
    """

    # Define the variables for the query
    variables = {
        "address": address,
        "language": language,
        "queryLimit": query_limit,
        "distanceUnit": distance_unit,
        "placeId": place_id,
        "sessionToken": session_token
    }

    # Make the request
    response = requests.post(
        url,
        headers=headers,
        json={'operationName': 'geocodeHotelSummaryOptions', 'query': query, 'variables': variables}
    )

    # Check for a successful response
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query failed with status code {response.status_code}: {response.text}")
