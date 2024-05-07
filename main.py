import importlib.util
from Contracts.Models.GCPPrivateOfferMessageModel import GCPPrivateOfferMessage

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
    module.run_selenium_script2()
