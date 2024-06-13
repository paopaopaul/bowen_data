import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure Selenium to use a visible browser window
options = Options()
options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
# options.add_argument("--headless")  # Make sure to comment or remove this line to see the browser

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://seller-us-accounts.tiktok.com/account/login")
    input("Please log in manually in the browser and press Enter in this console once you are logged in...")
    print("Login successful. Continuing with the script...")
    driver.get("https://affiliate-us.tiktok.com/connection/creator?source_from=seller_affiliate_landing&shop_region=US")
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'tr.sc-hzhJZQ.eSyGBZ.cursor-pointer')))
    table_rows = driver.find_elements(By.CSS_SELECTOR, 'tr.sc-hzhJZQ.eSyGBZ.cursor-pointer')
    all_row_data = [row.text for row in table_rows]

    structured_data = []
    for profile in all_row_data:
        lines = profile.split('\n')  # Assuming each piece of data is separated by newlines
        name_index = 1 if "Fast growing" not in lines[1] else 2  # Default to line 2, adjust to line 1 if no "Fast growing"

        data = {
            "Username": re.search(r"^\S+", lines[0]),
            "Growth_status": re.search(r"(\bFast growing\b|\bStable\b|\bDeclining\b)", lines[1]),
            "Name": lines[name_index] if len(lines) > name_index else "Unavailable",  # Direct assignment as it's not a regex match
            "Category": re.search(r"Beauty & Personal Care", profile),
            "Additional_info": re.search(r", \+\d", profile),
            "Demographics(followers,gender ratio,age)": re.search(r"(\d+(\.\d+)?K?), \w+ \d+%, \d+-\d+", profile),
            "GMV": re.search(r"\$\d+\.?\d*K?", profile),
            "Units Sold": re.search(r"(\d+\.?\d*K?)", profile),
            "Avg. video views": re.search(r"(\d+\.?\d*K?)", profile),
            "Engagement rate": re.search(r"(\d+\.?\d*%)", profile)
        }

        # Ensuring only valid matches are processed, else assign 'Unavailable'
        for key, match in data.items():
            if key != "Name":  # Skip 'Name' since it's not a regex match and is handled above
                data[key] = match.group(0) if match else "Unavailable"

        structured_data.append(data)

    # Print structured data
    for data in structured_data:
        print(data)

finally:
    driver.quit()
