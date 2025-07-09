import requests

# Vault URL and token
vault_url = 'http://vault.default.svc.cluster.local:8200'  # Replace with your Vault URL
vault_token = 'your-vault-token'  # Replace with your Vault token

# Vault API endpoint for reading a secret
secret_path = 'secret/myapp/config'  # Replace with your secret path

# Headers for Vault token authentication
headers = {
    'X-Vault-Token': vault_token
}

# URL to get the secret from the KV v2 engine
url = f'{vault_url}/v1/{secret_path}'

# Make a GET request to the Vault API
response = requests.get(url, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    secret = response.json()
    print("Successfully retrieved the secret:")
    print(f"Secret: {secret['data']['data']}")  # Access the data inside the secret
else:
    print(f"Failed to retrieve secret: {response.status_code}")
    print(response.text)
