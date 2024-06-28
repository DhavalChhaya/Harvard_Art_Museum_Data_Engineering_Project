import requests
import os

# Replace with your actual API key
api_key = os.getenv('api_key')

# Base URL
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

# Iterate through each resource
for resource in resources:
    print(f"Fetching total records for {resource.capitalize()}")  # Capitalize resource name for better readability

    # Parameters for the API request to get total records count
    params = {
        'apikey': api_key,
        'size': 1  # Fetch only one record to get total count
    }

    # Make the request to get total records count
    response = requests.get(f"{base_url}{resource}", params=params)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        total_records = data.get('info', {}).get('totalrecords', 0)

        # Calculate number of pages based on total records and page size (assuming default size of 100)
        if total_records > 0:
            page_size = 100  # Adjust based on API's pagination limit if different
            num_pages = (total_records + page_size - 1) // page_size  # Round up division

            print(f"Resource: {resource.capitalize()}, Total Records: {total_records}, Number of Pages: {num_pages}")
        else:
            print(f"No records found for {resource.capitalize()}")

    else:
        print(f"Error fetching total records for {resource.capitalize()}: {response.status_code} - {response.reason}")


