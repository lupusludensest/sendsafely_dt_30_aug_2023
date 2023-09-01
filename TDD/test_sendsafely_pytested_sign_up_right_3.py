from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import string

def test_sendsafely_pytested_sign_up_right_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://www.sendsafely.com")
    wait = WebDriverWait(driver, 15)

    # Click button "Accept" cookies
    driver.find_element(*ACPT_CCKS_BTN).click()

    # 1 Click button "Sign up Now"
    driver.find_element(*SGN_P_BTN).click()

    # 2 Enter the email randomized to "Email address" empty field
    def generate_random_email():
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"{username}@{domain}"
        return email

    # Generate random email, login, and password
    random_email = generate_random_email()

    print(f"\nRandom Email: {random_email}")

    # Send randomly generated email to cleansed and empty email field
    empty_email_field = driver.find_element(*EML_ADDRSS_FLD)
    empty_email_field.clear()
    empty_email_field.send_keys(random_email)

    # 3 Click on "Get Started" button
    driver.find_element(*GT_STRTD_BTN).click()

    # 4 Verify "https://www.sendsafely.com/auth/#signup" is open
    driver.find_element(*GT_STRTD_BTN)
    if driver.current_url == 'https://www.sendsafely.com/auth/#signup':
        print(f'\nhttps://www.sendsafely.com/auth/#signup is here')
    else:
        print(f'\nhttps://www.sendsafely.com/auth/#signup is not here')
    driver.back()

    driver.quit()