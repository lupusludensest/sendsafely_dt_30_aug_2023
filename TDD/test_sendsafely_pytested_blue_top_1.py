from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sendsafely_pytested_blue_top_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://www.sendsafely.com")
    wait = WebDriverWait(driver, 15)

    # Click button "Accept" cookies
    driver.find_element(*ACPT_CCKS_BTN).click()

    # 1 Picture SENDSAFELY '/img/ss_logo_60_343.png' is present
    snd_sfl_pctr = wait.until(EC.visibility_of_element_located(SND_SFL_PCTR)) # driver.find_element(*SND_SFL_PSTR)
    if '/img/ss_logo_60_343.png' in snd_sfl_pctr.get_attribute('src'):
        print(f'\nImage SENDSAFELY is visible on screen')
    else:
        print(f'\nImage SENDSAFELY is not visible on screen')

    # 2 Picture Globe as a Schema '/img/globe_lines.png' is present
    glb_s_schm_pctr = wait.until(EC.visibility_of_element_located(GLB_S_SCHM_PCTR))
    if '/img/globe_lines.png' in glb_s_schm_pctr.get_attribute('src'):
        print(f'\nImage Globe as a Schema is visible on screen')
    else:
        print(f'\nImage Globe as a Schema is not visible on screen')

    # 3 Text "The end-to-end encryption platform for modern business" is here
    e2e_txt_encrptn_txt = driver.find_element(*E2E_TXT_ECRPTN_TXT)
    expected_text = "The end-to-end encryption platform for modern business"
    actual_text = (e2e_txt_encrptn_txt).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 4 "Features" button is here
    ftrs_btn = driver.find_element(*FTRS_BTN)
    expected_text = "Features"
    actual_text = (ftrs_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 5 "Solutions" button is here
    sltns_btn = driver.find_element(*SLTNS_BTN)
    expected_text = "Solutions"
    actual_text = (sltns_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 6 "Pricing" button is here
    prcng_btn = driver.find_element(*PRCN_BTN)
    expected_text = "Pricing"
    actual_text = (prcng_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 7 "How It Works" button is here
    hw_t_wrks_btn = driver.find_element(*HW_T_WRKS_BTN)
    expected_text = "How it Works"
    actual_text = (hw_t_wrks_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 8 "Blog" button is here
    blg_btn = driver.find_element(*BLG_BTN)
    expected_text = "Blog"
    actual_text = (blg_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 9 "Log In" button is here
    lgn_btn = driver.find_element(*LGN_BTN)
    expected_text = "Log In"
    actual_text = (lgn_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 10 "Request Demo" button is here
    rqst_dm_btn = driver.find_element(*RQST_DM_BTN)
    expected_text = "Request Demo"
    actual_text = (rqst_dm_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 11 "Sign up Now" button is here
    sgn_p_btn = driver.find_element(*SGN_P_BTN)
    expected_text = "Sign up Now"
    actual_text = (sgn_p_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 12 "Learn More " button is here
    lrn_mr_btn = driver.find_element(*LRN_MR_BTN)
    expected_text = "Learn More"
    actual_text = (lrn_mr_btn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    driver.quit()


