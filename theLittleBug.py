from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')  # Suppresses console output

# Setting up ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://affiliate-us.tiktok.com/connection/creator?source_from=seller_affiliate_landing&shop_region=US")
print(driver.title) # Output: TikTok Shop Affiliate

driver.quit()

