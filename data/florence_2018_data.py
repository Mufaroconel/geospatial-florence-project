import requests
import json

# Hurricane Florence JSON URL
url = "https://flhurricane.com/cyclone/stormhistory.php?j=1&year=2018&storm=6"
print("Requesting data from:", url)

# Download the JSON data
response = requests.get(url)
print("Status code:", response.status_code)

# Check if request was successful
if response.status_code == 200:
    print("Saving data to florence_2018.json")
    # Save to file
    with open('florence_2018.json', 'w') as f:
        json.dump(response.json(), f, indent=4)
    print("JSON data saved to florence_2018.json")
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print("Response text:", response.text)