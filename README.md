# UK Trade Data Comprehensive Scraper

A comprehensive Python script to download **ALL** available UK trade data from the UK Trade Info website.

## Description

This project scrapes the UK Trade Info website to download the complete collection of UK trade datasets, including current data, historical archives, and regional statistics. It downloads **83 files totaling ~1.3GB** of trade data.

## Features

- **Complete Coverage**: Downloads from 3 main data sources
  - Latest bulk datasets (current monthly data)
  - Historical archive datasets (2016-2025)
  - Regional trade statistics (2013-2025)
- **Organized Storage**: Files are automatically organized into categorized subdirectories
- **Progress Tracking**: Shows download progress with file counts and completion status
- **Size Reporting**: Displays file sizes and total download size
- **Error Handling**: Robust error handling for failed downloads
- **Comprehensive Summary**: Detailed breakdown of what was downloaded

## Requirements

- Python 3.6+
- requests
- beautifulsoup4

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd UK_Trade
```

2. Install required packages:
```bash
pip install requests beautifulsoup4
```

## Data Sources

The scraper downloads from three main sources:

### 1. Latest Bulk Datasets (6 files, ~23MB)
- Control files (commodity codes and units)
- Current month exports data
- Current month imports data
- Importer details
- Exporter details
- Import data by preference

### 2. Historical Archive Datasets (61 files, ~1.2GB)
- **Control Files**: 2016-2025 (commodity code descriptions)
- **Exports**: Annual data 2016-2025
- **Imports**: Semi-annual data 2016-2025
- **Importer Details**: Historical importer information
- **Exporter Details**: Historical exporter information
- **Preference Data**: Import preference data 2021-2025

### 3. Regional Trade Statistics (16 files, ~41MB)
- **Current Quarters**: Q1 2024 - Q1 2025 (TXT files)
- **Historical Annual**: 2013-2023 (ZIP files)

## Usage

Run the comprehensive scraper:
```bash
python scrape_for_csvs.py
```

The script will:
1. Create organized directory structure (`uk_trade_data/`)
2. Download from all three data sources sequentially
3. Show progress for each category
4. Provide detailed completion summary

**⚠️ Note**: This downloads ~1.3GB of data and may take several minutes.

## Output Structure

```
uk_trade_data/
├── latest_bulk_datasets/     # Current monthly data (6 files)
├── archive_datasets/         # Historical data 2016-2025 (61 files)
└── regional_datasets/        # Regional statistics 2013-2025 (16 files)
```

## License

This project is open source and available under the [MIT License](LICENSE).
