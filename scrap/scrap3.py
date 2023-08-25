import csv
import requests
from bs4 import BeautifulSoup

def addProduct(url):
    try:
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

        all_info["URL"] = url

        # Create a CSV file and append data
        with open('flipkart_AC.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['In The Box', 'Brand', 'Model Name', 'Type', 'Capacity in Tons', 'Star Rating', 'BEE Rating Year', 'Color', 'Cooling and Heating', 'Cooling Capacity', 'Compressor', 'Dehumidification', 'Remote Control', 'Refrigerant', 'Operating Modes', 'Condenser Coil', 'Indoor W x H x D', 'Indoor Unit Weight', 'Outdoor W x H x D', 'Outdoor Unit Weight', 'Panel Display', 'Indoor Temperature Indicator', 'Turbo Mode', 'ISEER', 'Auto Air Swing', 'Anti-bacteria Filter', 'Dust Filter', 'Active Carbon Filter', 'Deodorizing Filter', 'Other Filter Features', 'Power Requirement', 'Annual Electricity Consumption', 'URL']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the values to the CSV file, ignoring fields not in fieldnames
            filtered_info = {key: value for key, value in all_info.items() if key in fieldnames}
            writer.writerow(filtered_info)
    except Exception as e:
        pass
urls = ['https://www.flipkart.com/whirlpool-convertible-5-in-1-cooling-2023-model-2-ton-3-star-split-inverter-6th-sense-technology-ac-white/p/itm26c0c0b111cfd?pid=ACNGHUJBQRXFTBHH&lid=LSTACNGHUJBQRXFTBHHHXHZTP&marketplace=FLIPKART&q=air+condictioner+above+5000+cooling+capacity&store=j9e%2Fabm&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=e99ecce5-b61a-4502-8ce9-0b3dbd660d04.ACNGHUJBQRXFTBHH.SEARCH&ppt=sp&ppn=sp&ssid=t4927qqz7k0000001692861549869&qH=c2567d99db439e8c','https://www.flipkart.com/godrej-5-in-1-convertible-cooling-2023-model-2-ton-5-star-split-inverter-4-way-air-swing-ac-white/p/itm7354d41d50dcc?pid=ACNGNSBERZSRWGGZ&lid=LSTACNGNSBERZSRWGGZ0PIPYX&marketplace=FLIPKART&q=air+condictioner+above+5000+cooling+capacity&store=j9e%2Fabm&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=e99ecce5-b61a-4502-8ce9-0b3dbd660d04.ACNGNSBERZSRWGGZ.SEARCH&ppt=sp&ppn=sp&ssid=t4927qqz7k0000001692861549869&qH=c2567d99db439e8c','https://www.flipkart.com/lg-ai-convertible-6-in-1-cooling-2023-model-2-ton-3-star-split-dual-inverter-4-way-swing-hd-filter-anti-virus-protection-ac-white/p/itm38ade154590cd?pid=ACNGHBX4KVAZFZ4E&lid=LSTACNGHBX4KVAZFZ4EBAHMQL&marketplace=FLIPKART&q=air+condictioner+above+5000+cooling+capacity&store=j9e%2Fabm&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=e99ecce5-b61a-4502-8ce9-0b3dbd660d04.ACNGHBX4KVAZFZ4E.SEARCH&ppt=sp&ppn=sp&ssid=t4927qqz7k0000001692861549869&qH=c2567d99db439e8c','https://www.flipkart.com/carrier-flexicool-convertible-4-in-1-cooling-2-ton-3-star-split-inverter-dual-filtration-hd-pm2-5-filter-ac-white/p/itm9a9083d94decb?pid=ACNGA3G2HMUFASRZ&lid=LSTACNGA3G2HMUFASRZCHJR9F&marketplace=FLIPKART&q=air+condictioner+above+5000+cooling+capacity&store=j9e%2Fabm&srno=s_1_5&otracker=search&otracker1=search&fm=Search&iid=e99ecce5-b61a-4502-8ce9-0b3dbd660d04.ACNGA3G2HMUFASRZ.SEARCH&ppt=sp&ppn=sp&ssid=t4927qqz7k0000001692861549869&qH=c2567d99db439e8c','https://www.flipkart.com/ifb-fastcool-convertible-8-in-1-cooling-2023-model-2-ton-3-star-split-inverter-smart-ready-7-stage-air-treatment-ac-white/p/itmeafde026da893?pid=ACNGKQGADUW5GCRY&lid=LSTACNGKQGADUW5GCRYJYAS5P&marketplace=FLIPKART&q=air+condictioner+above+5000+cooling+capacity&store=j9e%2Fabm&srno=s_1_6&otracker=search&otracker1=search&fm=Search&iid=e99ecce5-b61a-4502-8ce9-0b3dbd660d04.ACNGKQGADUW5GCRY.SEARCH&ppt=sp&ppn=sp&ssid=t4927qqz7k0000001692861549869&qH=c2567d99db439e8c','https://www.flipkart.com/samsung-convertible-5-in-1-cooling-2023-model-2-ton-3-star-split-inverter-ac-wi-fi-connect-white/p/itm549ce8efa1f27?pid=ACNGHRDQMBEJ7UY9&lid=LSTACNGHRDQMBEJ7UY90VHJIW&marketplace=FLIPKART&q=air+condictioner+above+5000+cooling+capacity&store=j9e%2Fabm&srno=s_1_7&otracker=search&otracker1=search&fm=Search&iid=e99ecce5-b61a-4502-8ce9-0b3dbd660d04.ACNGHRDQMBEJ7UY9.SEARCH&ppt=sp&ppn=sp&ssid=t4927qqz7k0000001692861549869&qH=c2567d99db439e8c']

for i in urls:
    addProduct(i)