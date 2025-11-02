import requests
import os
import argparse
import json

SHIMMIE_URL = "http://my-booru-url"

USERNAME = "USER"

# IMPORTANT: This is not your password.
# For GraphQL to work, you need to enable User's API Keys in your board config.
# After that, check your profile and your key will be at the bottom.
API_KEY = "API_KEY"

def upload_image_graphql(file_path, tags, source_url):
    upload_url = f"{SHIMMIE_URL}/graphql_upload?api_key={API_KEY}"
    print(f"Attempting upload to GraphQL API: {upload_url.split('?')[0]}") 

    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    data = {
        'tags': tags,
        'tags0': tags, 
    }
    
    if source_url:
        data['source'] = source_url 
    
    try:
        with open(file_path, "rb") as f:
            files = {
                'data0': (os.path.basename(file_path), f)
            }

            print(f"Uploading '{file_path}'...")
            print(f"  Tags: {tags}")
            if source_url:
                print(f"  Source: {source_url}")
            
            response = requests.post(upload_url, data=data, files=files)

            print(f"\nResponse Code: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    json_response = response.json()
                    print("Upload successful! Server Response (JSON):")
                    print(json.dumps(json_response, indent=2))

                    if 'data' in json_response and 'upload' in json_response['data']:
                         print("\nCLUE: GraphQL 'data' field found. Upload likely succeeded.")
                    elif 'errors' in json_response:
                         print("\nERROR: GraphQL response contains errors (check the JSON above).")

                except requests.exceptions.JSONDecodeError:
                    print("Error: Received 200 OK, but response was NOT valid JSON.")
                    print("This usually means a PHP error/warning was printed before the GraphQL output.")
                    print("\n--- FULL RAW RESPONSE TEXT (CHECK FOR PHP ERRORS) ---")
                    print(response.text)
                    print("---------------------------------------------------------------")
                    
            elif response.status_code >= 400:
                print(f"Upload failed: {response.status_code}")
                print("Response Text:", response.text)
            
            else:
                print(f"Unexpected status code: {response.status_code}")
                print(f"Response Text: {response.text}")

    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a file to a Shimmie2 instance using the GraphQL API.")
    
    parser.add_argument("file_path", 
                        help="The path to the file you want to upload.")
    
    parser.add_argument("-t", "--tags", 
                        help="A space-separated string of tags.", 
                        required=True)
    
    parser.add_argument("-s", "--source", 
                        help="Optional: The source URL for the image.", 
                        default="")
    
    args = parser.parse_args()

    if "your_username" in USERNAME or "your_api_key" in API_KEY:
        print("Error: Please update 'USERNAME' and 'API_KEY' in the script before running.")
    else:
        upload_image_graphql(args.file_path, args.tags, args.source)
