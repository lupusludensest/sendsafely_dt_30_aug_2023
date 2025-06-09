from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import logging

from app.application import Application

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def browser_init(context):
    """
    :param context: Behave context
    """
    try:
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Commented out to see the browser
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--start-maximized")  # Changed to a more standard resolution
        # or try chrome_options.add_argument("--start-maximized")  # This will maximize the browser window
        chrome_options.add_argument("--remote-debugging-port=9222")

        # Install ChromeDriver using WebDriver Manager with cache_valid_range
        # driver_path = ChromeDriverManager(cache_valid_range=1).install()
        driver_path = "C:\\Webdrivers\\chromedriver.exe"
        logger.info(f"ChromeDriver path: {driver_path}")

        service = ChromeService(driver_path)
        context.driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )

        context.driver.implicitly_wait(4)
        context.app = Application(context.driver)

        # Verify driver is working
        logger.info(f"Chrome version: {context.driver.capabilities['browserVersion']}")
        logger.info(f"ChromeDriver version: {context.driver.capabilities['chrome']['chromedriverVersion']}")

    except WebDriverException as e:
        logger.error(f"Failed to initialize WebDriver: {str(e)}")
        raise


def before_scenario(context, scenario):
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    logger.info(f'\nStarted step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'\nStep failed: {step}')
        # Optionally take screenshot on failure
        if hasattr(context, 'driver'):
            try:
                context.driver.save_screenshot(f"failed_step_{step.name}.png")
            except Exception as e:
                logger.error(f"Could not take screenshot: {str(e)}")


def after_scenario(context, scenario):
    try:
        if hasattr(context, 'driver'):
            context.driver.delete_all_cookies()
            context.driver.quit()
    except Exception as e:
        logger.error(f"Error in cleanup: {str(e)}")