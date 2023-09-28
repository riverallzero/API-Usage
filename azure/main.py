from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time

subscription_key = 'azure_computervision_api_key'
endpoint = 'azure_computervision_endpoint'

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

image_path = 'image_path'
local_image = open(image_path, 'rb')

read_response = computervision_client.read_in_stream(local_image, raw=True)
read_operation_location = read_response.headers['Operation-Location']
operation_id = read_operation_location.split('/')[-1]

while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

text_results = []
if read_result.status == OperationStatusCodes.succeeded:
    text_results = [line.text for text_result in read_result.analyze_result.read_results for line in
                    text_result.lines]

print(text_results)
