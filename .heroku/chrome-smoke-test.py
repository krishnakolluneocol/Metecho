import selenium
import selenium.webdriver
import sys
soptions = selenium.webdriver.chrome.options.Options()
soptions.headless = True
try:
    driver = selenium.webdriver.Chrome(options=soptions)
    driver.quit()
    print(f"Able to open chrome")
except Exception as e:
    print(f"Unable to open chrome:\n{e}")
    sys.exit(1) 