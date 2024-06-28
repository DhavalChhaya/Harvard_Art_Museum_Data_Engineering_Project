import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

# Replace with your actual API key
api_key = os.getenv('api_key')
base_url = 'https://api.harvardartmuseums.org/'

# List of resources to iterate through
resources = [
    "object",
    "person",
    "exhibition",
    "publication",
    "gallery",
    "spectrum",
    "classification",
    "century",
    "color",
    "culture",
    "group",
    "medium",
    "support",
    "period",
    "place",
    "technique",
    "worktype",
    "activity",
    "site",
    "video",
    "image",
    "audio",
    "annotation"
]

# Directory to save the data files
output_dir = 'D:\Project\Harvard-Art_Museum'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to fetch and save data
def fetch_and_save(resource):
    page = 1
    max_pages = 200  # Limit to 200 pages
    has_records = True

    # Create a directory for the current resource
    resource_dir = os.path.join(output_dir, resource)
    if not os.path.exists(resource_dir):
        os.makedirs(resource_dir)

    while has_records and page <= max_pages:
        print(f"Fetching data for {resource.capitalize()}, page {page}")

        # Parameters for the API request
        params = {
            'apikey': api_key,
            'size': 100,  # Number of records per page (adjust as per API limit)
            'page': page  # Current page number
        }

        # Make the request
        response = requests.get(f"{base_url}{resource}", params=params)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])

            # If there are records, save data to a file
            if records:
                # Create filename and save data to the specified directory
                filename = os.path.join(resource_dir, f"{resource}_page{page}.json")
                with open(filename, 'w') as f:
                    json.dump(records, f, indent=4)

                print(f"Data saved locally: {filename}")

                # Move to the next page
                page += 1
            else:
                # No more records, exit loop
                has_records = False
                print(f"No more records found for {resource.capitalize()}. Process stopped.")

        else:
            print(f"Error fetching data for {resource.capitalize()}, page {page}: {response.status_code} - {response.reason}")
            break  # Exit loop on error

# Fetch and save data for each resource
for resource in resources:
    fetch_and_save(resource)
