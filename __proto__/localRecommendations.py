import hashlib
import hmac
import requests
from datetime import datetime, timezone

# Constants
base_url = "https://hmsstg.hiltonapi.com/hms/v1/"
method_signature = "core/localRecommendations"
querystring = {"ctyhocn": "DCAOTHF"}
secret_key = "52tBVaCe"
app_key = "hhonors"
device_id = "a235c98737c63559"

def get_utc_datetime():
    return datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="milliseconds") + "Z"

def get_hms_api_headers():
    current_utc_datetime = get_utc_datetime()
    headers = {
        "appkey": app_key,
        "hmac-sha1": "60455484d94c53ca2a130626dfd09591a13f3fb5",
        "timestamp": current_utc_datetime,
        "deviceid": device_id,
        "accept": "application/json",
    }
    return headers

def get_hms_hmac(secret_key, current_utc_datetime, method_endpoint):
    signature_string = f"{secret_key.decode()}&{current_utc_datetime}&{method_signature}".encode()  # Convert to byte string
    hmac_sha1 = hmac.new(secret_key, signature_string, hashlib.sha1)    
    hmac_result = hmac_sha1.hexdigest()
    return hmac_result

def get_local_recommendations():
    session = requests.Session()
    session.headers.update(get_hms_api_headers())
    url = f"{base_url}{method_signature}"
    
    response = session.get(url, params=querystring, verify=False)  # Disable SSL verification
    
    # Printing the full request details for debugging
    print("Full Request URL:", response.request.url)
    print("Request Headers:", response.request.headers)
    if response.request.body:
        print("Request Body:", response.request.body)
    
    # Check the response status and content
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Failed to retrieve data:", response.status_code, response.text)

if __name__ == "__main__":
    get_local_recommendations()
