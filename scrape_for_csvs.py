import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Settings
BASE_URL = "https://www.uktradeinfo.com/trade-data/"
DOWNLOAD_DIR = "uk_trade_csvs"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Get all CSV links
r = requests.get(BASE_URL)
soup = BeautifulSoup(r.text, 'html.parser')

csv_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.endswith('.csv') and 'commodity-and-country' in href:
        full_url = urljoin(BASE_URL, href)
        csv_links.append(full_url)

# Download CSVs
downloaded_files = []
for url in csv_links:
    file_name = os.path.join(DOWNLOAD_DIR, os.path.basename(url))
    print(f"Downloading {url}")
    try:
        r = requests.get(url)
        with open(file_name, "wb") as f:
            f.write(r.content)
        downloaded_files.append(file_name)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

print(f"\nDownload complete! {len(downloaded_files)} CSV files saved to '{DOWNLOAD_DIR}' directory.")
if downloaded_files:
    print("Downloaded files:")
    for file in downloaded_files:
        print(f"  - {file}")