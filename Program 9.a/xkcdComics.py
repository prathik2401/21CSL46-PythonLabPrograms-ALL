import requests
import os
from bs4 import BeautifulSoup

# Set the initial URL
url = 'https://xkcd.com/1/'

# Create a directory for storing comics
os.makedirs('xkcd_comics', exist_ok=True)

while True:
    # Send an HTTP GET request
    res = requests.get(url)
    res.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(res.text, 'html.parser')

    # Find the comic image element
    comic_elem = soup.select_one('#comic img')

    if comic_elem:
        # Construct the comic image URL
        comic_url = 'https:' + comic_elem['src'] 

        # Send a request to download the image
        res = requests.get(comic_url)
        res.raise_for_status()

        # Save the image in the 'xkcd_comics' directory
        with open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb') as image_file:
            image_file.write(res.content)

    # Find the URL of the previous comic
    prev_link = soup.select_one('a[rel="prev"]')

    if not prev_link:
        break

    # Update the URL for the next iteration
    url = 'https://xkcd.com' + prev_link['href'] 
    print("Downloading",comic_url)

print('All comics downloaded.')