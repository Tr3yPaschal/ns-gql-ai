import requests
import hashlib
import hmac 
import urllib3
import ssl
import datetime
from collections import namedtuple
from datetime import datetime

base_url = "https://hmsstg.hiltonapi.com/hms/v1/"
method_signature = "core/localRecommendations"
querystring = {"ctyhocn": "DCAOTHF"}
secret_key = "52tBVaCe"
#secret_key = "MySecretKey"
app_key = "hhonors"
device_id = "a235c98737c63559"

def get_hms_hmac(key, message):
    # Create a new HMAC object using the provided key and SHA1 hash algorithm
    hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha1)
    
    # Return the hexadecimal digest of the HMAC object
    return hmac_obj.hexdigest()

def get_utc_datetime():
    return datetime.utcnow().isoformat(timespec="milliseconds") + "Z"

def get_hms_api_headers(appkey,secret,method_signature_hash):
    current_utc_datetime = datetime.utcnow().isoformat(timespec="milliseconds") + "Z"
    headers = {
        "appkey": appkey,
       #"hmac-sha1": get_hms_hmac(secret,current_utc_datetime,method_signature_hash),
        "hmac-sha1" : get_hms_hmac(secret,message_text),
        "timestamp": current_utc_datetime
    }
    return headers

time = get_utc_datetime()
message_text = (secret_key + "&" + time + "&"  + method_signature  )
print("Message Text: ",message_text)

#print(get_hmac_sha1(secret_key,message_text))
print(get_hms_hmac(secret_key,message_text))
print(get_hms_api_headers(app_key,secret_key,method_signature))

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

request_session = None

if request_session is None:
    request_session = requests.Session()
    request_session.verify=False

else:
    request_session = request_session
    request_session.verify=False


response = None

# Update the session headers
request_session.headers.update(get_hms_api_headers(app_key, secret_key, method_signature))

# Send a GET request
full_url = base_url + method_signature
response = request_session.get(full_url, params=querystring)

print("Full Request URL:", response.request.url)
print(" ")
print(request_session.headers)
print(" ")
print(response.status_code)
#print(response.text)
print(response.json())

