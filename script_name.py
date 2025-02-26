import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin


def get_product_details(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        print(f"Fetching URL: {url}")
        product_name = url.strip('/').split('/')[-1]
        print(f"Extracted product name from URL: {product_name}")

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize product data dictionary
        product_data = {
            'Name': product_name,
            'Category': 'Network Cameras',
            'Description': None,
            'Stock': 1,
            'Is Available': True,
            'Is Featured': False,
            'Is Published': True,
            # Camera Specifications
            'Max Resolution': None,
            'Sensor': None,
            'Day Night': None,
            'Shutter': None,
            'Adjustment Angle': None,
            'S/N': None,
            'WDR': None,
            # Lens Specifications
            'Focal Length': None,
            'Iris Type': None,
            'Iris': None,
            # Video Specifications
            'Video Compression': None,
            'Frame Rate': None,
            'Video Bit Rate': None,
            'Video Stream': None,
            # Audio Specifications
            'Audio Compression': None,
            'Two Way Audio': None,
            'Suppression': None,
            'Sampling Rate': None,
            # Storage
            'Edge Storage': None,
            'Network Storage': None,
            # Network
            'Protocols': None,
            'Compatible Integration': None,
            # General Specifications
            'Power': None,
            'Dimensions': None,
            'Weight': None,
            'Material': None,
            # Images
            'Photo Main': None,
            'Photo 1': None,
            'Photo 2': None,
            'Photo 3': None,
            'Photo 4': None
        }

        # Image processing code remains the same
        images = []
        possible_selectors = [
            'img.product-image',
            'img.gallery-image',
            '.product-gallery img',
            '.product-detail img',
            'img[src*="product"]',
        ]
        
        for selector in possible_selectors:
            images.extend(soup.select(selector))
        
        seen = set()
        images = [x for x in images if not (x.get('src') in seen or seen.add(x.get('src')))]
        
        for idx, img in enumerate(images[:5]):
            img_url = img.get('src')
            if img_url:
                if not img_url.startswith('http'):
                    img_url = urljoin(url, img_url)
                if idx == 0:
                    product_data['Photo Main'] = img_url
                else:
                    product_data[f'Photo {idx}'] = img_url

        # Product name and description processing remains the same
        product_name = soup.find('h1')
        if product_name:
            product_data['Name'] = product_name.text.strip()

        description_points = soup.find_all('li')
        if description_points:
            product_data['Description'] = '\n'.join(
                [point.text.strip() for point in description_points])

        # Updated specification mapping
        spec_table = soup.find('table')
        if spec_table:
            rows = spec_table.find_all('tr')
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 2:
                    key = cols[0].text.strip()
                    value = cols[1].text.strip()

                    mapping = {
                        'Max Resolution': 'Max Resolution',
                        'Sensor': 'Sensor',
                        'Day/Night': 'Day Night',
                        'Shutter': 'Shutter',
                        'Adjustment Angle': 'Adjustment Angle',
                        'S/N': 'S/N',
                        'WDR': 'WDR',
                        'Focal Length': 'Focal Length',
                        'Iris Type': 'Iris Type',
                        'Iris': 'Iris',
                        'Video Compression': 'Video Compression',
                        'Frame Rate': 'Frame Rate',
                        'Video Bit Rate': 'Video Bit Rate',
                        'Video Stream': 'Video Stream',
                        'Audio Compression': 'Audio Compression',
                        'Two-way Audio': 'Two Way Audio',
                        'Suppression': 'Suppression',
                        'Sampling Rate': 'Sampling Rate',
                        'Edge Storage': 'Edge Storage',
                        'Network Storage': 'Network Storage',
                        'Protocols': 'Protocols',
                        'Compatible Integration': 'Compatible Integration',
                        'Power': 'Power',
                        'Dimensions': 'Dimensions',
                        'Weight': 'Weight',
                        'Material': 'Material'
                    }

                    if key in mapping:
                        product_data[mapping[key]] = value

        if all(v is None for v in product_data.values()):
            print("Warning: No data was extracted from the page")
            return None

        return product_data

    except Exception as e:
        print(f"Error processing URL {url}: {str(e)}")
        return None


def main():
    try:
        # Read URLs from file
        with open('urls.txt', 'r') as file:
            urls = [line.strip() for line in file if line.strip()
                    and not line.startswith('#')]

        if not urls:
            print("No valid URLs found in urls.txt")
            return

        print(f"Found {len(urls)} URLs to process")

        # List to store all product data
        all_products = []

        # Process each URL
        for url in urls:
            print(f"\nProcessing: {url}")
            product_data = get_product_details(url)
            if product_data:
                all_products.append(product_data)
                print(
                    f"Successfully extracted data for {product_data.get('Name', 'Unknown Product')}")
            time.sleep(2)  # Be nice to the server

        # Create DataFrame and save to Excel
        if all_products:
            print(f"\nCreating Excel file with {len(all_products)} products")
            df = pd.DataFrame(all_products)
            df.to_excel('product_import_template.xlsx', index=False)
            print("Data successfully saved to product_import_template.xlsx")
        else:
            print("No data was collected - Excel file not created")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
