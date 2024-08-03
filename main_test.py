from config.driver_config import get_driver, close_driver, setup_logger
from page_objects.amazon_search import AmazonSearchPage
import time

def test_search_and_extract_product_details():
    logger = setup_logger()
    driver = get_driver()
    amazon_page = AmazonSearchPage(driver)
    try:
        amazon_page.open_home_page()
        amazon_page.search_for_product("echo dot")
        all_links = amazon_page.get_all_product_links()
        if all_links:
            first_product_details = amazon_page.get_product_details(all_links[0])
            logger.info("First Product Details:")
            for key, value in first_product_details.items():
                logger.info(f"{key}: {value}")
        else:
            logger.info("No products found.")
    finally:
        time.sleep(5)  # Give time to review before closing the browser
        close_driver(driver)

if __name__ == "__main__":
    test_search_and_extract_product_details()
