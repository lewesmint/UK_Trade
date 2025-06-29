# UK Trade Data Scraper

A Python script to download UK trade data CSV files from the UK Trade Info website.

## Description

This project scrapes the UK Trade Info website (https://www.uktradeinfo.com/trade-data/) to download CSV files containing commodity and country trade data.

## Features

- Automatically finds and downloads CSV files containing 'commodity-and-country' data
- Saves files to a local directory (`uk_trade_csvs`)
- Provides download progress and completion summary
- Error handling for failed downloads

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

## Usage

Run the scraper:
```bash
python scrape_for_csvs.py
```

The script will:
1. Connect to the UK Trade Info website
2. Find all CSV links containing 'commodity-and-country'
3. Download them to the `uk_trade_csvs` directory
4. Display a summary of downloaded files

## Output

Downloaded CSV files will be saved in the `uk_trade_csvs` directory in the same location as the script.

## License

This project is open source and available under the [MIT License](LICENSE).
