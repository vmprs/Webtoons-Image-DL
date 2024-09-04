import requests

# URL of the image
url = "insert url of the image here"

# Make the HTTP request
headers = {'Referer': 'http://www.webtoons.com/'}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Save the image to a file
    with open('downloaded_image.jpg', 'wb') as file:
        file.write(response.content)
    print("Image downloaded successfully!")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
