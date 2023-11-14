import selenium
import selenium.webdriver
import sys
soptions = selenium.webdriver.chrome.options.Options()
soptions.headless = True
soptions.add_argument("--no-sandbox")
soptions.add_argument("--headless")
soptions.add_argument("--disable-dev-shm-usage")
soptions.add_argument('--disable-gpu')
soptions.add_argument('--remote-debugging-port=9222')
try:
    driver = selenium.webdriver.Chrome(options=soptions)
    driver.quit()
    print(f"Able to open chrome")
except Exception as e:
    print(f"Unable to open chrome:\n{e}")
    sys.exit(1) 