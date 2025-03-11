import random
import pandas as pd
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#rotating user agents
useragents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
]
#defining headers to make the requests look authentic
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}
#initializing the bot
def initialize_driver():
    options = {
        "uc": True,
        "headless": False 
    }
    driver = Driver(**options)
    
    # Set the user agent using uc_cdp_events
    custom_user_agent = random.choice(useragents)
    driver.uc_cdp_events = [
        ("Network.setUserAgentOverride", {"userAgent": custom_user_agent})
    ]
    
    return driver
#defining scraper function
def scrape_reviews(max_pages=None):
    base_url = "your-company-url"
    reviewgroup = []
    driver = initialize_driver()
#iterating through pages
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scraping page {page}")
#bypassing cloudflare
        driver.uc_open_with_reconnect(url, 10)
        driver.uc_gui_click_captcha()
        time.sleep(15)
#waittime before loading
        wait = WebDriverWait(driver, 15)
        reviews = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ab_comp_review_card")))
#cleaning reviews before appending to list
        for review in reviews:
            reviewgroup.append(review.text.strip())
#to go to next page
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.page-nav-btn[href*='page=']")))
            if "disabled" in next_button.get_attribute("class"):
                print("Reached last page")
                break
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
        except Exception as e:
            print(f"Error navigating to next page: {e}")
            break
#quiting driver
    driver.quit()
    return reviewgroup

# Main execution
reviews = scrape_reviews(max_pages=32)

# Print reviews
for i, r in enumerate(reviews, 1):
    print(f"{i}. {r}\n")

# Create DataFrame and export to CSV
df = pd.DataFrame(reviews, columns=['Review'])
df.to_csv('your_company_reviews.csv', index=False)
print("Reviews exported to your_company_reviews.csv")
