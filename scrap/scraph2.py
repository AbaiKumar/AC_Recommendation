import requests
from bs4 import BeautifulSoup
import csv

# URL of the Flipkart product page
url = 'https://www.flipkart.com/carrier-1-5-ton-5-star-split-inverter-ac-white/p/itm23c012a2d5f9c?pid=ACNGG54VYZXZXZ5V&lid=LSTACNGG54VYZXZXZ5VBBKCUC&marketplace=FLIPKART&q=CARRIER+1.5+Ton+5+Star+Split+Inverter+AC++-+White&store=j9e%2Fabm%2Fc54&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=395d37c5-79df-438a-8558-afdb95b5621c.ACNGG54VYZXZXZ5V.SEARCH&ppt=None&ppn=None&ssid=adxyjl2lfk0000001692377844775&qH=a42c9754bdfffb44'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize a dictionary to store all information
all_info = {}

# Extract general information
general_div = soup.find('div', class_='_3k-BhJ')
for row in general_div.find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    all_info[key] = ', '.join(value)

# Extract dimensions information
dimensions_div = soup.find('div', class_='flxcaE', string='Dimensions')
for row in dimensions_div.find_next('table', class_='_14cfVK').find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    all_info[key] = ', '.join(value)

# Extract performance features information
performance_features_div = soup.find('div', class_='flxcaE', string='Performance Features')
for row in performance_features_div.find_next('table', class_='_14cfVK').find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    all_info[key] = ', '.join(value)

# Extract air flow & filter features information
air_flow_filter_features_div = soup.find('div', class_='flxcaE', string='Air Flow & Filter Features')
for row in air_flow_filter_features_div.find_next('table', class_='_14cfVK').find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    all_info[key] = ', '.join(value)

# Extract power features information
power_features_div = soup.find('div', class_='flxcaE', string='Power Features')
for row in power_features_div.find_next('table', class_='_14cfVK').find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    all_info[key] = ', '.join(value)

# Write the extracted information to a CSV file
with open('flipkart_AC.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=all_info.keys())
    writer.writeheader()
    writer.writerow(all_info)
