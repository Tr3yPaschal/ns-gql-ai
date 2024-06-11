import hmac
import hashlib
from datetime import datetime, timezone

secret_key = b"52tBVaCe"  # Note the 'b' prefix to make it a byte string
current_utc_datetime = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="milliseconds") + "Z"
method_signature = "core/localRecommendations"

signature_string = f"{secret_key.decode()}&{current_utc_datetime}&{method_signature}".encode()  # Convert to byte string

# Create HMAC SHA-1
hmac_sha1 = hmac.new(secret_key, signature_string, hashlib.sha1)

# Get the hexadecimal representation of the HMAC
hmac_result = hmac_sha1.hexdigest()

print(hmac_result)
