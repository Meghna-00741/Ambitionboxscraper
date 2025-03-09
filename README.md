# Ambitionboxscraper
This bot helps scrape company reviews from up to 60 pages on Ambition Box

# UPS Employee Reviews Scraper

This project is a web scraper designed to collect employee reviews from AmbitionBox for UPS Logistics. It utilizes SeleniumBase for automated browsing and bypassing security measures.

## Features

- Rotates user agents for anonymity.
- Uses SeleniumBase to handle browser automation and CAPTCHA bypassing.
- Extracts and cleans employee reviews.
- Supports pagination to scrape multiple pages.
- Saves the extracted reviews as a CSV file.

## Requirements

Ensure you have the following installed:

- Python 3.x
- SeleniumBase
- pandas

Install dependencies using:

```bash
pip install seleniumbase pandas
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/yourusername/company-reviews-scraper.git
cd company-reviews-scraper
```

2. Run the script:

```bash
python ambnbox6.py
```

3. The script will extract reviews and save them in `UPS_reviews.csv`.

## Configuration

- **Max Pages**: You can modify the `max_pages` parameter in `scrape_reviews(max_pages=32)` to adjust the number of pages to scrape.
- **Headless Mode**: Change `headless=False` to `headless=True` in `initialize_driver()` to run in headless mode.

## Output

- The reviews are saved in a CSV file named `company_reviews.csv`.
- Each review is stored in a structured format within a Pandas DataFrame.

## Disclaimer

- This scraper is intended for educational and research purposes only.
- Ensure compliance with AmbitionBox's Terms of Service before running the scraper.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

how 

