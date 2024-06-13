from selenium import webdriver
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
    # Replace the URL below with the actual login page URL
    driver.get("https://seller-us-accounts.tiktok.com/account/login")

    # Pause the script for manual login
    input("Please log in manually in the browser and go to the site you wish to bug. \nPress Enter in this console once you are logged in...")

    # Print a message to the console to indicate that the script will now resume
    print("Login successful. Continuing with the script...")

    # Your subsequent automation logic goes here

finally:
    # Ensure the driver quits when you're done or if an error occurs
    driver.quit()
