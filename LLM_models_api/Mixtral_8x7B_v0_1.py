import requests
api_token = "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" 
def run_inference(prompt, api_token="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"):
    # Define the API endpoint and model name
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    

    # Prepare the request headers with the API token
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # Prepare the request payload
    payload = {
        "inputs": prompt
    }

    # Make the POST request to the inference API
    response = requests.post(API_URL, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
    
        return result
    else:
        print("Error:", response.status_code)
        return None

# Example usage
# prompt = input("Enter your prompt")


# inference_result = run_inference(prompt, api_token)
# if inference_result is not None:
#     print("Inference result:", inference_result)
# else:
#     print("Failed to get inference result.")
