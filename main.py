import importlib.util
import json
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

# Load configuration from JSON file
with open('keyvaultsconfig.json') as keyvaultsconfig_file:
    keyvaultsconfig = json.load(keyvaultsconfig_file)

# Your Azure Key Vault URL
key_vault_url = keyvaultsconfig['KeyVaultURL']

# Your Application (Client) ID
client_id = keyvaultsconfig['ClientID']

# Your Application (Client) Secret
client_secret = keyvaultsconfig['ClientSecret']

# Your Azure Active Directory Tenant ID
tenant_id = keyvaultsconfig['TenantID']

# Create an instance of ClientSecretCredential with your client ID, client secret, and tenant ID
credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)

# Create a SecretClient using the Key Vault URL and the ClientSecretCredential
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Retrieve a secret by its name
secret_name = "Cloud-SaaS-Kit-GCP-SVC"
secret_value = client.get_secret(secret_name)

secret_value = secret_value.value

# Suppose this is the condition based on which you decide which Selenium script to run
condition = False

if condition:
    module_path = 'WorkflowStepProcessors/GCPSeleniumRequestProcessorV1'
else:
    module_path = 'WorkflowStepProcessors/GCPSeleniumRequestProcessorV2'

# Dynamically import the module
spec = importlib.util.spec_from_file_location(module_path, f"{module_path}.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Call the appropriate function based on the condition
if condition:
    module.run_selenium_script1()
else:
    module.run_selenium_script2(secret_value)
