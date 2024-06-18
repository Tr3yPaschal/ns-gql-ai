import requests
from collections import namedtuple
import json
import urllib3
import ssl
import html
import hashlib
import hmac 
import csv
import datetime

class HMS_API :
    def __init__(self, base_url, method_signature, querystring, secret_key, app_key, device_id, request_session=None):
   
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ssl._create_default_https_context = ssl._create_unverified_context

        self.base_url = base_url
        self.method_signature = method_signature
        self.querystring = querystring
        self.secret_key = secret_key
        self.app_key = app_key
        self.device_id = device_id

        if request_session is None:
            self.request_session = requests.Session()
            self.request_session.verify=False

        else:
            self.request_session = request_session
            self.request_session.verify=False

    ResponseOutcome = namedtuple('ResponseOutcome', ['has_error', 'response_code', 'response_value'])           

    def handle_response(self, response):

        response_value = ""
        has_error = False

        if response.status_code == 200:
            try:
                response_value = response.json()
            except json.JSONDecodeError:
                has_error = True
                response_value = "Invalid JSON response"
        elif response.status_code == 201:
            response_value = "Created"
        elif response.status_code == 204:
            response_value = "Operation completed successfully with no additional content."
        elif response.status_code in (403, 404, 415):
            has_error = True
            response_value = html.unescape(response.text)
        elif response.status_code == 500:
            has_error = True
            response_value = response.text
        else:
            has_error = True
            response_value = response.text

        return self.ResponseOutcome(has_error=has_error, response_code=response.status_code, response_value=response_value)
    
    def set_json_attribute(self):
        self.request_session.headers.update(get_hms_api_headers(self.app_key, self.secret_key, self.method_signature))
        this_url = f"{self.base_url}/{self.method_signature}/{self.querystring}"
        
        requestBody = {
            "publish": True,
            "publishDescendants": True,
            "attribute": {
                "value": json.dumps(attribute_json)  # Convert Python dictionary to JSON formatted string
            }
        }
        
        print("Request URL:", this_url)
        print("Request Body:", requestBody)
        
        response = self.request_session.put(this_url, json=requestBody)
        
        # Debugging: Print out the full response details
        print("Response Status Code:", response.status_code)
        print("Response Text:", response.text)
        
        return self.handle_response(response)
    
def get_hms_api_headers(app_key,secret_key,method_signature_hash):

    current_utc_datetime = datetime.datetime.utcnow().isoformat(timespec="milliseconds") + "Z"

    headers = {
        "appkey": app_key,
        "hmac-sha1": get_hms_hmac(secret_key,current_utc_datetime,method_signature_hash),
        "timestamp": current_utc_datetime
    }
    return headers

def get_hms_hmac(secret_key,current_utc_datetime,method_signature_hash):

    message_text = (secret_key + "&" + current_utc_datetime  + "&"  + method_signature_hash  )
    h = hashlib.new('sha1')
    secret_key=bytes(secret_key,'UTF-8')
    message=bytes(message_text,'UTF-8')
    digester = hmac.new(secret_key, message, hashlib.sha1)
    hmac_sha1=digester.hexdigest()
    return hmac_sha1
