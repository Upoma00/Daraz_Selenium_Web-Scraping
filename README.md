
# Project
# Daraz Smartphone Scraper
This Python script scrapes smartphone data from the Daraz website using Selenium WebDriver and saves it to a CSV file
# Prerequisites
Make sure you have the following installed on your system:

Selenium library

Pandas library

Webdriver_manager library
You can install the required libraries using pip:

## pip install selenium pandas webdriver_manager
# How to Use
Clone the repository or download the scraper.py file.

Run the scraper.py script:

The script will start scraping smartphone data from multiple pages on the Daraz website and save it to a file named daraz_smartphone.csv.

# Note
The script uses Chrome WebDriver. Make sure you have ChromeDriver installed and added to your system PATH.

The script will scrape data from pages 1 to 9. You can modify the range in the for page in range(1, 10) loop to scrape more or fewer pages as needed.

The website structure might change over time, so the script may need adjustments in the XPath selectors if it stops working.

For any issues or improvements, feel free to contribute or raise an issue in this repository.
