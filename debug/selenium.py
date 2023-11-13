from selenium import webdriver

def test_chrome_driver():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(90)

    driver.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CAD')

    min_exchange_rate = 1.3
    max_exchange_rate = 1.4

    element = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[3]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/p[2]')

    exchange_rate = float(element.text.split(' ')[0])

    driver.quit()  # maybe close instead?

if __name__ == "__main__":
    test_chrome_driver()