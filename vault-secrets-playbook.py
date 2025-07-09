import hvac

# Connect to Vault
client = hvac.Client(url='http://vault.default.svc.cluster.local:820')  # Update URL to match your Vault instance

# Authenticate (you can authenticate via token, AppRole, etc.)
client.token = 'your-vault-token'  # Use your Vault token here

# Check if the client is authenticated
if client.is_authenticated():
    print("Successfully authenticated to Vault")
else:
    print("Authentication failed")

# Retrieve a secret from Vault (replace with your secret path)
secret = client.secrets.kv.v2.read_secret_version(path='secret/myapp/config')

# Print the secret
print(f"Secret: {secret['data']['data']}")
