import requests

# URL of the image
url = "https://webtoon-phinf.pstatic.net/20181223_133/1545540580475SXbeO_JPEG/b748a7cf-e5bc-448b-8945-5a277b9ef486.jpg?type=q90"

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
