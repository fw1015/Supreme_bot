from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeit

full_name = "Wan Fong Ching Founder"
email = "xxxxxxxx@gmail.com"

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

chrome_driver_path = "/Users/Founder/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
driver.get("https://www.supremenewyork.com/shop/all")

def bot():
    element = driver.find_element_by_xpath("/html/body/div[2]/nav/ul/li[11]/a")
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Supreme®/Sea to Summit Self Inflating Sleeping Mat"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "commit"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "checkout now"))
    )
    element.click()

    # name_field = driver.find_element_by_id("order_billing_name")
    # name_field.send_keys(full_name)

if __name__ == "__main__":
    print(timeit.timeit(bot, number=1))

