import requests
from bs4 import BeautifulSoup

# URL of the Flipkart product page
url = 'https://www.flipkart.com/carrier-1-5-ton-5-star-split-inverter-ac-white/p/itm23c012a2d5f9c?pid=ACNGG54VYZXZXZ5V&lid=LSTACNGG54VYZXZXZ5VBBKCUC&marketplace=FLIPKART&q=CARRIER+1.5+Ton+5+Star+Split+Inverter+AC++-+White&store=j9e%2Fabm%2Fc54&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=395d37c5-79df-438a-8558-afdb95b5621c.ACNGG54VYZXZXZ5V.SEARCH&ppt=None&ppn=None&ssid=adxyjl2lfk0000001692377844775&qH=a42c9754bdfffb44'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the div containing general information
general_div = soup.find('div', class_='_3k-BhJ')

# Initialize a dictionary to store the extracted information
ac_info = {}

# Iterate through each row in the table
for row in general_div.find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    ac_info[key] = value

# Print the extracted information
for key, value in ac_info.items():
    print(f"{key}: {value}")

#        dimension
# Find the div containing dimensions information
dimensions_div = soup.find('div', class_='flxcaE', string='Dimensions')

# Initialize a dictionary to store the extracted dimensions
dimensions_info = {}

# Iterate through each row in the dimensions table
for row in dimensions_div.find_next('table', class_='_14cfVK').find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    dimensions_info[key] = value

# Print the extracted dimensions information
for key, value in dimensions_info.items():
    print(f"{key}: {value}")

#    performance
# Find the div containing performance features information
performance_features_div = soup.find('div', class_='flxcaE', string='Performance Features')

# Initialize a dictionary to store the extracted performance features
performance_features_info = {}

# Iterate through each row in the performance features table
for row in performance_features_div.find_next('table', class_='_14cfVK').find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    performance_features_info[key] = value

# Print the extracted performance features information
for key, value in performance_features_info.items():
    print(f"{key}: {value}")


# Find the div containing air flow & filter features information
air_flow_filter_features_div = soup.find('div', class_='flxcaE', string='Air Flow & Filter Features')

# Initialize a dictionary to store the extracted air flow & filter features
air_flow_filter_features_info = {}

# Iterate through each row in the air flow & filter features table
for row in air_flow_filter_features_div.find_next('table', class_='_14cfVK').find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    air_flow_filter_features_info[key] = value

# Print the extracted air flow & filter features information
for key, value in air_flow_filter_features_info.items():
    print(f"{key}: {value}")

# Find the div containing power features information
power_features_div = soup.find('div', class_='flxcaE', string='Power Features')

# Initialize a dictionary to store the extracted power features
power_features_info = {}

# Iterate through each row in the power features table
for row in power_features_div.find_next('table', class_='_14cfVK').find_all('tr', class_='_1s_Smc row'):
    key = row.find('td', class_='_1hKmbr col col-3-12').text.strip()
    value = [item.text.strip() for item in row.find('td', class_='URwL2w col col-9-12').find_all('li')]
    power_features_info[key] = value

# Print the extracted power features information
for key, value in power_features_info.items():
    print(f"{key}: {value}")