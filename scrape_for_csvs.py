import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Settings
BASE_URL = "https://www.uktradeinfo.com/trade-data/latest-bulk-datasets/"
DOWNLOAD_DIR = "uk_trade_csvs"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Get all CSV and ZIP links from the bulk datasets page
print(f"Fetching UK Trade bulk datasets from: {BASE_URL}")
r = requests.get(BASE_URL)
soup = BeautifulSoup(r.text, 'html.parser')

csv_links = []
zip_links = []

for link in soup.find_all('a', href=True):
    href = link['href']
    # Check for CSV files
    if href.endswith('.csv'):
        full_url = urljoin(BASE_URL, href)
        csv_links.append(full_url)
    # Check for ZIP files (which contain CSV data)
    elif href.endswith('.zip'):
        full_url = urljoin(BASE_URL, href)
        zip_links.append(full_url)

# Combine all download links
all_download_links = csv_links + zip_links
print(f"Found {len(csv_links)} CSV files and {len(zip_links)} ZIP files to download")

# Download all files (CSV and ZIP)
downloaded_files = []
for url in all_download_links:
    file_name = os.path.join(DOWNLOAD_DIR, os.path.basename(url))
    print(f"Downloading {url}")
    try:
        r = requests.get(url)
        with open(file_name, "wb") as f:
            f.write(r.content)
        downloaded_files.append(file_name)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

print(f"\nDownload complete! {len(downloaded_files)} files saved to '{DOWNLOAD_DIR}' directory.")
if downloaded_files:
    print("Downloaded files:")
    for file in downloaded_files:
        file_size = os.path.getsize(file) / (1024 * 1024)  # Size in MB
        print(f"  - {os.path.basename(file)} ({file_size:.1f} MB)")