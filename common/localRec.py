import requests
import hashlib
import hmac
import urllib3
import ssl
from datetime import datetime

base_url = "https://hmsstg.hiltonapi.com/hms/v1/"
method_signature = "core/localRecommendations"
secret_key = "52tBVaCe"
app_key = "hhonors"

class LocalRec:
    def __init__(self, ctyhocn):
        self.ctyhocn = ctyhocn

    def get_hms_hmac(self, key, message):
        hmac_obj = hmac.new(key.encode(), message.encode(), hashlib.sha1)
        return hmac_obj.hexdigest()

    def get_utc_datetime(self):
        return datetime.utcnow().isoformat(timespec="milliseconds") + "Z"

    def get_hms_api_headers(self, appkey, secret, method_signature_hash):
        current_utc_datetime = self.get_utc_datetime()
        headers = {
            "appkey": appkey,
            "hmac-sha1": self.get_hms_hmac(secret, current_utc_datetime + method_signature_hash),
            "timestamp": current_utc_datetime
        }
        return headers

    def get_local_recommendations(self):
        time = self.get_utc_datetime()
        message_text = secret_key + "&" + time + "&" + method_signature
        querystring = {"ctyhocn": self.ctyhocn}

        session = requests.Session()
        session.headers.update(self.get_hms_api_headers(app_key, secret_key, message_text))
        url = f"{base_url}{method_signature}"

        response = session.get(url, params=querystring, verify=False)
        print("Message Text: ", message_text)

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        ssl._create_default_https_context = ssl._create_unverified_context

        print("Full Request URL:", response.request.url)
        print(" ")
        print(session.headers)
        print(" ")
        print(response.status_code)
        print(" ")
        return response.json()