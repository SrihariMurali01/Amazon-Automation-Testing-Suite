from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonSearchPage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):
        self.driver.get("https://www.amazon.in")

    def search_for_product(self, product_name):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_input.clear()
        search_input.send_keys(product_name + Keys.RETURN)

    def get_all_product_links(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".s-result-item.s-asin"))
        )
        products = self.driver.find_elements(By.CSS_SELECTOR, ".s-result-item.s-asin")
        links = [product.find_element(By.CSS_SELECTOR, "h2 a").get_attribute('href') for product in products]
        return links

    def get_product_details(self, product_url):
        self.driver.get(product_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "productTitle"))
        )
        details = {}
        details['title'] = self.driver.find_element(By.ID, "productTitle").text.strip()
        try:
            details['price'] = self.driver.find_element(By.ID, "priceblock_ourprice").text.strip()
        except:
            details['price'] = "Price not available"
        details['availability'] = self.driver.find_element(By.ID, "availability").text.strip()
        details['description'] = self.driver.find_element(By.ID, "feature-bullets").text.strip()
        return details
