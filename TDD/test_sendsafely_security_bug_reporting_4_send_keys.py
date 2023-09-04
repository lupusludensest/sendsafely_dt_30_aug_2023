from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import string
from pynput.keyboard import Key, Controller
import pyautogui
from selenium.webdriver.common.keys import Keys

def test_sendsafely_security_bug_reporting_form_4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://www.sendsafely.com")
    wait = WebDriverWait(driver, 15)

    # Click button "Accept" cookies
    driver.find_element(*ACPT_CCKS_BTN).click()

    # 1 Click button "Security Overview"
    driver.find_element(*SCRT_RVW_BTN).click()

    # 2 Scroll down and click button "Security Bug Reporting Form"
    scrt_bg_rprtng_frm_btn = driver.find_element(*SCRT_BG_RPRTNG_FRM_BTN)
    actions = ActionChains(driver)
    actions.move_to_element(scrt_bg_rprtng_frm_btn).click()
    actions.perform()

    # 3 Verify field "Enter your email address" is here. Enter the email randomized to "Enter your email address" empty field.
    entr_yr_eml_addrss_fld = wait.until(EC.visibility_of_element_located(ENTR_YR_EML_ADDRSS_FLD))
    if 'Enter your email address' in entr_yr_eml_addrss_fld.get_attribute('placeholder'):
        print(f'\n"Enter your email address" is visible on screen')
    else:
        print(f'\n"Enter your email address" is not visible on screen')

    def generate_random_email():
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"{username}@{domain}"
        return email

    # Generate random email, login, and password
    random_email = generate_random_email()
    print(f'\nRandom Email: "1 {random_email}"')

    empty_email_field = driver.find_element(*ENTR_YR_EML_ADDRSS_FLD)
    empty_email_field.clear()
    empty_email_field.send_keys(f'1{random_email}')


    # 4 Verify field "What category of security bug is this?" is here. Enter the "test bug" to "What category of security bug is this?" empty field.
    wht_ctgry_f_scrt_bg_fld = wait.until(EC.visibility_of_element_located(WHT_CTGRY_F_SCRT_BG_FLD))
    if 'What category of security bug is this?' in wht_ctgry_f_scrt_bg_fld.get_attribute('placeholder'):
        print(f'\n"2 What category of security bug is this?" is visible on screen')
    else:
        print(f'\n"2 What category of security bug is this?" is not visible on screen')

    empty_test_bug_field = driver.find_element(*WHT_CTGRY_F_SCRT_BG_FLD)
    empty_test_bug_field.clear()
    empty_test_bug_field.send_keys("2 test bug category")

    # 5 Verify field "Provide the URL that is affected" is here
    url_affctd_fld = wait.until(EC.visibility_of_element_located(URL_AFFCTD_FLD))
    if 'Provide the URL that is affected' in url_affctd_fld.get_attribute('placeholder'):
        print(f'\n"3 Provide the URL that is affected" is visible on screen')
    else:
        print(f'\n"3 Provide the URL that is affected" is not visible on screen')

    empty_url_field = driver.find_element(*URL_AFFCTD_FLD)
    empty_url_field.clear()
    empty_url_field.send_keys("3 https://www.sendsafely.com/security/bug-report/")

    # 6 Verify field "Provide a descriptive bug caption" is here
    dscrptv_bg_cptn_fld = wait.until(EC.visibility_of_element_located(DSCRPTV_BG_CPTN_FLD))
    if 'Provide a descriptive bug caption' in dscrptv_bg_cptn_fld.get_attribute('placeholder'):
        print(f'\n"4 Provide a descriptive bug caption" is visible on screen')
    else:
        print(f'\n"4 Provide a descriptive bug caption" is not visible on screen')

    empty_dscrptv_field = driver.find_element(*DSCRPTV_BG_CPTN_FLD)
    empty_dscrptv_field.clear()
    empty_dscrptv_field.send_keys("4 test bug description")

    # 7 Verify field "Describe how we can replicate this issue" is here
    dscrptv_hw_cn_rplc_fld = wait.until(EC.visibility_of_element_located(DSCRPTV_HW_CN_RPLC_FLD))
    if 'Describe how we can replicate this issue' in dscrptv_hw_cn_rplc_fld.get_attribute('placeholder'):
        print(f'\n"5 Describe how we can replicate this issue" is visible on screen')
    else:
        print(f'\n"5 Describe how we can replicate this issue" is not visible on screen')

    empty_rplc_field = driver.find_element(*DSCRPTV_HW_CN_RPLC_FLD)
    empty_rplc_field.clear()
    empty_rplc_field.send_keys("5 test bug replication")

    # 8 Verify field "Put any additional information that you think we might find useful here" is here
    addtnl_inf_mght_b_usf_fld = wait.until(EC.visibility_of_element_located(ADDTNL_INF_MGHT_B_USL_FLD))
    if 'Put any additional information that you think we might find useful here' in addtnl_inf_mght_b_usf_fld.get_attribute('placeholder'):
        print(f'\n"6 Put any additional information that you think we might find useful here" is visible on screen')
    else:
        print(f'\n"6 Put any additional information that you think we might find useful here" is not visible on screen')

    empty_mght_field = driver.find_element(*ADDTNL_INF_MGHT_B_USL_FLD)
    empty_mght_field.clear()
    empty_mght_field.send_keys("6 test bug additional information")

    # 9 Scroll down and click button "Drag files here or click to add file"
    iframes = driver.find_elements(By.TAG_NAME, 'iframe')
    print(f'\ncurrent url: {driver.current_url}\nlen of iframes: {len(iframes)}\ntype of iframe: {type(iframes)}')
    iframe = iframes[0]
    driver.switch_to.frame(iframe)
    sleep(4)
    print(f'current url: {driver.current_url}\ntype of iframe: {type(iframe)}')
    # Click on or send keys to button "Drag files here or click to add file"
    actions = ActionChains(driver)
    drg_fls_clck_add_fl_btn = driver.find_element(*DRG_FLS_CLCK_ADD_FL_BTN)
    # File path specified to send N.B. Whenever I sent a path it is always landed to "Additional Information" field
    actions.move_to_element(drg_fls_clck_add_fl_btn).send_keys(r"C:\Users\rapid\test_send_bug_report.jpg")
    sleep(2)
    actions.perform()

    driver.switch_to.default_content()

    driver.find_element(*SBMT_BTN).click()

    sleep(4)
    driver.quit()

