# nyt-scraper

This Python script downloads the front page of The New York Times in PDF format and converts it into a high-quality JPEG image. It allows you to save the front page for the current day or the previous day if the current day's front page is not available.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)
- `PIL` (Python Imaging Library) (install via `pip install pillow`)
- `pdf2image` library (install via `pip install pdf2image`)

## Usage

1. Install the required libraries mentioned above.
2. Run the script `nyt_scraper.py`.
3. The script will attempt to download the front page for the current day.
4. If the front page for the current day is not available, it will attempt to download the front page for the previous day.
5. The resulting high-quality JPEG image of the front page will be saved in the same directory as the script with a filename following the format `nyt-YYYYMMDD.jpg`, where `YYYYMMDD` is the date of the front page.
