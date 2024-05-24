# Full disclosure - I did not write this code. My friend wrote this code for his own project & I shamelessly stole it :)

import asyncio
import time

from logzero import logger

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

urls = [
    {
        "url": "https://jack-hopper.streamlit.app/",
        "name": "Jack Hopper Website",
    }
]


async def open_app(url, service):

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    logger.info(f"Opening {url['name']} at {url['url']}...")

    driver = webdriver.Chrome(service=Service(service), options=chrome_options)

    # Go to url
    driver.get(url["url"])
    logger.info(f"{url['name']} is sleeping at {url['url']}...")

    # Wait for 2 minutes
    await asyncio.sleep(60)

    # Close the browser
    driver.close()
    logger.info(f"Closed {url['name']} at {url['url']}")
    return 200


async def main(urls):
    """Open webpage on list of urls concurrently"""
    service = ChromeDriverManager().install()
    start = time.time()
    # Run everything concurrently
    await asyncio.gather(*(open_app(url, service) for url in urls))
    logger.info(f"Finished in {time.time() - start} seconds")


if __name__ == "__main__":
    asyncio.run(main(urls))