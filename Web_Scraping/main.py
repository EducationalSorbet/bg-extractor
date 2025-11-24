import requests
from url_parse import urlparse
from os import makedirs
from sys import exit
from Tabular import clean_print
# URL of the websites you want to scrape
url = str(input("Enter URL: "))
file_name = str(input("Enter file_name: "))

# Test the function
parsed_url = urlparse(url)

# Print out the components
print("|" + "-"*(4+len(url)) + "|")
clean_print(dict(parsed_url.items()))
print("|" + "-"*(4+len(url)) + "|")

# from urllib.parse import urlparse

def is_valid_url(url):
    parsed_url = urlparse(url)
    # Check if the URL has both a scheme (http/https) and a netloc (domain)
    return bool(parsed_url["Scheme"]) and bool(parsed_url["netloc"])

def write_source_code(file_name, path, source_code):
    # Making Required Dir(s) for downloading
    # css/arf.css
    if path != "":
        try:
            dir_lis = '/'.join(path.split("/")[:-1]) if "." in path.split("/")[-1] else '/'.join(path.split("/"))
            makedirs(dir_lis, exist_ok=True)
            print("just made this dir:", dir_lis)
        except OSError as e:
            print(f"Error creating directory path: {e}")
    
    
    # Writing File
    with open(file_name, "w+") as f:
        f.write(source_code)
    print("\tDONE WRITING..")


# Checking if a file is Valid
if is_valid_url(url):
    print(f">> {url} is a valid URL!")
else:
    print(f">> {url} is not a valid URL!")
    exit()
    print("ERROR \"THIS\" SHOULD NEVER BE PRINTED")

try:
    # Send an HTTP GET request to fetch the source code
    response = requests.get(url, timeout=10) # Timeout after 10 seconds

    # Check if the request to fetch the source code
    if response.status_code == 200:
        # Print the source code of the webpage
        source_code = response.text
        print(source_code) # This will print the HTML source code of the page
        # File_name
        print(parsed_url)
        path = parsed_url["path"] if parsed_url["path"] != parsed_url["netloc"] else ""
        if file_name == "":
            if "." in path.split("/")[-1]:
                file_name = path
            else:
                file_name = "Index.html"
        print("\n....Writing To", file_name.split("/")[-1], "\n\t\tin", path)
        write_source_code(file_name, path, source_code)
 
    else:
        print(f"Failed to retrive the page. Status code: {respons.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


