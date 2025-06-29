import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

# Settings
URLS = {
    "latest": "https://www.uktradeinfo.com/trade-data/latest-bulk-datasets/",
    "archive": "https://www.uktradeinfo.com/trade-data/latest-bulk-datasets/bulk-datasets-archive/",
    "regional": "https://www.uktradeinfo.com/trade-data/regional/regional-trade-statistics-datasets/"
}

BASE_DOWNLOAD_DIR = "uk_trade_data"
os.makedirs(BASE_DOWNLOAD_DIR, exist_ok=True)

# Create subdirectories for organization
SUBDIRS = {
    "latest": os.path.join(BASE_DOWNLOAD_DIR, "latest_bulk_datasets"),
    "archive": os.path.join(BASE_DOWNLOAD_DIR, "archive_datasets"),
    "regional": os.path.join(BASE_DOWNLOAD_DIR, "regional_datasets")
}

for subdir in SUBDIRS.values():
    os.makedirs(subdir, exist_ok=True)

def scrape_page_for_files(url, base_url, file_extensions=['.csv', '.zip', '.txt']):
    """Scrape a page for downloadable files with specified extensions"""
    print(f"Fetching data from: {url}")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    found_files = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        for ext in file_extensions:
            if href.endswith(ext):
                full_url = urljoin(base_url, href)
                found_files.append((full_url, ext))
                break

    return found_files

def download_files(file_list, download_dir, category_name):
    """Download a list of files to the specified directory"""
    downloaded_files = []

    print(f"\n=== Downloading {category_name} ===")
    print(f"Found {len(file_list)} files to download")

    for i, (url, ext) in enumerate(file_list, 1):
        file_name = os.path.join(download_dir, os.path.basename(url))
        print(f"[{i}/{len(file_list)}] Downloading {os.path.basename(url)}")

        try:
            r = requests.get(url)
            with open(file_name, "wb") as f:
                f.write(r.content)
            downloaded_files.append(file_name)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    return downloaded_files

# Scrape all data sources
all_downloaded = []

print("🇬🇧 UK Trade Data Comprehensive Scraper")
print("=" * 50)
print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# 1. Latest bulk datasets
latest_files = scrape_page_for_files(URLS["latest"], URLS["latest"])
latest_downloaded = download_files(latest_files, SUBDIRS["latest"], "Latest Bulk Datasets")
all_downloaded.extend(latest_downloaded)

# 2. Archive datasets (historical data)
archive_files = scrape_page_for_files(URLS["archive"], URLS["archive"])
archive_downloaded = download_files(archive_files, SUBDIRS["archive"], "Archive Datasets")
all_downloaded.extend(archive_downloaded)

# 3. Regional trade statistics
regional_files = scrape_page_for_files(URLS["regional"], URLS["regional"])
regional_downloaded = download_files(regional_files, SUBDIRS["regional"], "Regional Trade Statistics")
all_downloaded.extend(regional_downloaded)

# Summary
print("\n" + "=" * 50)
print("🎉 DOWNLOAD COMPLETE!")
print("=" * 50)
print(f"Total files downloaded: {len(all_downloaded)}")
print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Calculate total size and show breakdown
total_size = 0
category_stats = {
    "Latest": {"count": len(latest_downloaded), "size": 0},
    "Archive": {"count": len(archive_downloaded), "size": 0},
    "Regional": {"count": len(regional_downloaded), "size": 0}
}

for file_path in latest_downloaded:
    size = os.path.getsize(file_path) / (1024 * 1024)
    category_stats["Latest"]["size"] += size
    total_size += size

for file_path in archive_downloaded:
    size = os.path.getsize(file_path) / (1024 * 1024)
    category_stats["Archive"]["size"] += size
    total_size += size

for file_path in regional_downloaded:
    size = os.path.getsize(file_path) / (1024 * 1024)
    category_stats["Regional"]["size"] += size
    total_size += size

print(f"\nBreakdown by category:")
for category, stats in category_stats.items():
    print(f"  {category}: {stats['count']} files ({stats['size']:.1f} MB)")

print(f"\nTotal size: {total_size:.1f} MB")
print(f"\nFiles saved to: {BASE_DOWNLOAD_DIR}/")
print("  ├── latest_bulk_datasets/")
print("  ├── archive_datasets/")
print("  └── regional_datasets/")