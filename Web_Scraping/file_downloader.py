import requests

def download_file(url, save_path):
    """
    Downloads a file from the given URL and saves it locally.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error for bad status codes

        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                
                f.write(chunk)

        print(f"File downloaded successfully and saved as: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")



# Example usage
url = "https://testfileorg.netwet.net/500MB-CZIPtestfile.org.zip"
save_path = "500mb.zip"
download_file(url, save_path)
