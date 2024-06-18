import hmac
import hashlib
import requests
from datetime import datetime

# Provided values
base_url = "https://hmsstg.hiltonapi.com/hms/v1/"
method_value = "core/localRecommendations"
querystring = {"ctyhocn": "DCAOTHF"}
secret_key = "52tBVaCe"
app_key = "hhonors"
device_id = "a235c98737c63559"

# Generate current UTC time in ISO 8601 format
current_utc_time = datetime.utcnow().isoformat(timespec="milliseconds") + "Z"
print("Current UTC Time:", current_utc_time)

def get_hms_hmac(secret_key, current_utc_time, method_signature_hash):
    message_text = secret_key + "&" + current_utc_time + "&" + method_signature_hash
    print("HMAC Message Text:", message_text)
    secret_key_bytes = bytes(secret_key, 'UTF-8')
    message_bytes = bytes(message_text, 'UTF-8')
    digester = hmac.new(secret_key_bytes, message_bytes, hashlib.sha1)
    hmac_sha1 = digester.hexdigest()
    print("Generated HMAC SHA1:", hmac_sha1)
    return hmac_sha1

# Print the HMAC SHA1 to verify
print("HMAC SHA1 for Debug:", get_hms_hmac(secret_key, current_utc_time, method_value))

session = requests.Session()

# Set the necessary headers
headers = {
    'Accept': 'application/json',
    'appKey': app_key,
    'device-id': device_id,
    'hmac-sha1': get_hms_hmac(secret_key, current_utc_time, method_value),
    "timestamp": current_utc_time
}
print("Headers being used:", headers)
session.headers.update(headers)

# Make the GET request
response = session.get(f"{base_url}{method_value}", params=querystring)
print("Full Request URL:", response.request.url)
print("Request Headers:", response.request.headers)
print("Status Code:", response.status_code)
print("Response Text:", response.text)