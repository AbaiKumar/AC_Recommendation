import pandas as pd
from bs4 import BeautifulSoup
import requests

# Load CSV into a pandas DataFrame
csv_path = 'flipkart_AC.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_path)

# Create a list to store image URLs
image_urls = []

# Iterate through each URL in the DataFrame
for index, row in df.iterrows():
    url = row['URL']  # Replace 'URL' with the actual column name in your CSV
    
    # Send a GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.text
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the first <img> tag with the specified class name
    img = soup.find('img', class_='_396cs4 _2amPTt _3qGmMb')
    
    # Extract the 'src' attribute and add to the list
    if img:
        img_url = img.get('src').split(' ')
        image_urls.append(img_url)
        print(img_url)
    else:
        image_urls.append(None)  # If no image found, add None to the list

# Add the list of image URLs as a new column to the DataFrame
df['image_URL'] = image_urls

# Save the DataFrame back to the CSV file with the new column
df.to_csv(csv_path, index=False)