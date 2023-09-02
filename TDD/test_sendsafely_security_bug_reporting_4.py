from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string

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
        print(f'\nEnter your email address is visible on screen')
    else:
        print(f'\nEnter your email address is not visible on screen')

    def generate_random_email():
        domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"{username}@{domain}"
        return email

    # Generate random email, login, and password
    random_email = generate_random_email()
    print(f"\nRandom Email: {random_email}")

    empty_email_field = driver.find_element(*ENTR_YR_EML_ADDRSS_FLD)
    empty_email_field.clear()
    empty_email_field.send_keys(random_email)


    # 4 Verify field "What category of security bug is this?" is here. Enter the "test bug" to "What category of security bug is this?" empty field.
    wht_ctgry_f_scrt_bg_fld = wait.until(EC.visibility_of_element_located(WHT_CTGRY_F_SCRT_BG_FLD))
    if 'What category of security bug is this?' in wht_ctgry_f_scrt_bg_fld.get_attribute('placeholder'):
        print(f'\nWhat category of security bug is this? is visible on screen')
    else:
        print(f'\nWhat category of security bug is this? is not visible on screen')

    empty_test_bug_field = driver.find_element(*WHT_CTGRY_F_SCRT_BG_FLD)
    empty_test_bug_field.clear()
    empty_test_bug_field.send_keys("test bug")

    # 5 Verify field "Provide the URL that is affected" is here
    url_affctd_fld = wait.until(EC.visibility_of_element_located(URL_AFFCTD_FLD))
    if 'Provide the URL that is affected' in url_affctd_fld.get_attribute('placeholder'):
        print(f'\nProvide the URL that is affected is visible on screen')
    else:
        print(f'\nProvide the URL that is affected is not visible on screen')

    empty_url_field = driver.find_element(*URL_AFFCTD_FLD)
    empty_url_field.clear()
    empty_url_field.send_keys("https://www.sendsafely.com/security/bug-report/")

    # 6 Verify field "Provide a descriptive bug caption" is here
    dscrptv_bg_cptn_fld = wait.until(EC.visibility_of_element_located(DSCRPTV_BG_CPTN_FLD))
    if 'Provide a descriptive bug caption' in dscrptv_bg_cptn_fld.get_attribute('placeholder'):
        print(f'\nProvide a descriptive bug caption is visible on screen')
    else:
        print(f'\nProvide a descriptive bug caption is not visible on screen')

    empty_dscrptv_field = driver.find_element(*DSCRPTV_BG_CPTN_FLD)
    empty_dscrptv_field.clear()
    empty_dscrptv_field.send_keys("test bug dscrptv")

    # 7 Verify field "Describe how we can replicate this issue" is here
    dscrptv_hw_cn_rplc_fld = wait.until(EC.visibility_of_element_located(DSCRPTV_HW_CN_RPLC_FLD))
    if 'Describe how we can replicate this issue' in dscrptv_hw_cn_rplc_fld.get_attribute('placeholder'):
        print(f'\nDescribe how we can replicate this issue is visible on screen')
    else:
        print(f'\nDescribe how we can replicate this issue is not visible on screen')

    empty_rplc_field = driver.find_element(*DSCRPTV_HW_CN_RPLC_FLD)
    empty_rplc_field.clear()
    empty_rplc_field.send_keys("test bug hw_cn_rplc_fld")

    # 8 Verify field "Put any additional information that you think we might find useful here" is here
    addtnl_inf_mght_b_usf_fld = wait.until(EC.visibility_of_element_located(ADDTNL_INF_MGHT_B_USL_FLD))
    if 'Put any additional information that you think we might find useful here' in addtnl_inf_mght_b_usf_fld.get_attribute('placeholder'):
        print(f'\nPut any additional information that you think we might find useful here is visible on screen')
    else:
        print(f'\nPut any additional information that you think we might find useful here is not visible on screen')

    empty_mght_field = driver.find_element(*ADDTNL_INF_MGHT_B_USL_FLD)
    empty_mght_field.clear()
    empty_mght_field.send_keys("test bug mght")

    # 9 Scroll down and click button "Drag files here or click to add file"
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f'\nLen of iframes: {len(iframes)}\n{iframes}')
    # iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
    # driver.switch_to.frame(iframe)
    # driver.implicitly_wait(30)
    # driver.find_element(*DRG_FLSR_CLCK_ADD_FL_BTN).click()
    # driver.switch_to.default_content()

    # Iterate through the iframes
    for iframe in iframes:
        try:
            driver.switch_to.frame(iframe)
            # Check if the element you need is present in this iframe
            if driver.find_element(By.ID, "sendsafely-iframe"):
                # Interact with the element
                driver.find_element(By.ID, "sendsafely-iframe").click()
                break  # Exit the loop if the element is found
        except:
            # If switching to the iframe or finding the element fails, continue to the next iframe
            continue

    # Switch back to the default content
    driver.switch_to.default_content()

    sleep(4)
    driver.quit()

