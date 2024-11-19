from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from redmail import EmailSender
from itertools import product
import time

def wallapop_search(url, geckodriver_path):
    """
    Fetches ad titles and URLs from ads published today in Wallapop.de.

    Parameters:
    url (str): The URL of the page to scrape.
    geckodriver_path (str): The path to the Geckodriver executable.

    Returns:
    list of tuples: A list containing tuples of (title, url).
    """
    # Set up the Firefox WebDriver with options:
    options = Options()
    options.add_argument('-headless')  # Use headless mode (optional)

    # Use the specified path for the Geckodriver:
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    ads_data = []

    try:
        # Navigate to the target webpage
        driver.get(url)

        try:
            # Wait for the page to load and for the items to be present
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ItemCardList__item"))
            )
        except TimeoutException:
            # If no items load within the timeout, print message and return empty list
            #print("No items found.")
            return ads_data

        # Locate ads
        items = driver.find_elements(By.CLASS_NAME, "ItemCardList__item")

        # If no items are found, print message and return empty list
        if not items:
            #print("No items found.")
            return ads_data

        # Iterate through the located items and extract data
        for item in items:
            # Extract the title and URL for each ad
            title = item.get_attribute('title')
            ad_url = item.get_attribute('href')

            # Create a tuple and append it to the list
            ads_data.append((title, ad_url))

    finally:
        # Close the WebDriver
        driver.quit()

    # Print a summary after all items have been processed
    if ads_data:
        print(f"Found {len(ads_data)} items.")
    else:
        print("No items found.")

    return ads_data  # Return the collected data
