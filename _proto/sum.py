import requests
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import logging
import sys

# Suppress the output of the PyTorch model weights initialization message
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Make the GraphQL request
url = 'https://m.stg.hilton.io/graphql/customer?operationName=hotel&type=hotelDetails_LAXAVCI'
headers = {'Content-Type': 'application/json'}

# Prompt the user to enter the ctyhocn variable
ctyhocn = input("Enter the ctyhocn variable: ")

# Define the GraphQL query with the user-entered ctyhocn variable
data = {
    "operationName": "hotel",
    "variables": {
        "ctyhocn": ctyhocn,
        "language": "en-US"
    },
    "query": "query hotel($language: String!, $ctyhocn: String!) {\n  hotel(language: $language, ctyhocn: $ctyhocn) {\n    name\n    address {\n      addressFmt\n      addressLine1\n      addressLine2\n      city\n      country\n      postalCode\n      state\n    }\n    amenities {\n      name\n    }\n  }\n}\n"
}

response = requests.post(url, headers=headers, json=data)
response_data = response.json()

# Extract hotel data
hotel_data = response_data['data']['hotel']
hotel_name = hotel_data['name']
address_data = hotel_data['address']

# Check if address components are not None
address_components = [address_data[key] for key in ['addressLine1', 'addressLine2', 'city', 'state', 'postalCode', 'country']]
formatted_address = ', '.join(component for component in address_components if component)

amenities = [amenity['name'] for amenity in hotel_data['amenities']]

# Prepare input text
input_text = f"{hotel_name} is located at {formatted_address}. It offers amenities such as {' and '.join(amenities)}."

# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained("gpt2")

# Tokenize input text
input_ids = tokenizer.encode(input_text, return_tensors="tf")

# Generate summary
output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
hotel_summary = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Summary:")
print(hotel_summary)
