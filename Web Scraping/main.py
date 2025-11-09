import requests
from url_parse import urlparse
from pprint import pprint

# URL of the websites you want to scrape
url = str(input("Enter URL: "))

# Test the function
parsed_url = urlparse(url)

# Print out the components
print("|"+"-"*20+"|")
for key, value in parsed_url.items():
    print(f"|  {key.capitalize()}: {value}")
print("|"+"-"*20+"|")

# from urllib.parse import urlparse

def is_valid_url(url):
    parsed_url = urlparse(url)
    # Check if the URL has both a scheme (http/https) and a netloc (domain)
    return bool(parsed_url["Scheme"]) and bool(parsed_url["netloc"])


if is_valid_url(url):
    print(f"{url} is a valid URL!")
else:
    print(f"{url} is not a valid URL!")

try:
    # Send an HTTP GET request to fetch the source code
    response = requests.get(url, timeout=10) # Timeout after 10 seconds

    # Check if the request to fetch the source code
    if response.status_code == 200:
        # Print the source code of the webpage
        print(response.text) # This will print the HTML source code of the page
    else:
        print(f"Failed to retrive the page. Status code: {respons.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")



