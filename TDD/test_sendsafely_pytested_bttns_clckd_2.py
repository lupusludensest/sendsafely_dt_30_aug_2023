from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def test_sendsafely_pytested_bttns_clckd_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://www.sendsafely.com")
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # Click button "Accept" cookies
    driver.find_element(*ACPT_CCKS_BTN).click()

    # 1 Click "Features" button. Verify "https://www.sendsafely.com/features/" is open
    ftrs_btn = driver.find_element(*FTRS_BTN)
    ftrs_btn.click()
    if driver.current_url == 'https://www.sendsafely.com/features/':
        print(f'\nhttps://www.sendsafely.com/features/ is here')
    else:
        print(f'\nhttps://www.sendsafely.com/features/ is not here')
    driver.back()

    # 2 Hover over "Solutions" button. Verify 5 submenu items with texts are here
    sltns_btn = driver.find_element(*SLTNS_BTN)
    actions = ActionChains(driver)
    actions.move_to_element(sltns_btn).perform()
    fv_elmnts_drpdwn_mn_hr = driver.find_elements(*FV_ELMNTS_DRPDWN_MNU_HR)
    if len(fv_elmnts_drpdwn_mn_hr) == 5:
        print(f'\n5 elements are here')
    else:
        print(f'\nwrong output: {len(fv_elmnts_drpdwn_mn_hr)}')

    scr_eml = driver.find_element(*SCR_EML_TXT)
    expected_text = "Secure Email"
    actual_text = (scr_eml).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    hlp_dsk_intgrtn = driver.find_element(*HLP_DSK_INTGRTN_TXT)
    expected_text = "Help Desk Integrations"
    actual_text = (hlp_dsk_intgrtn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    scr_fl_exchng = driver.find_element(*SCR_FL_EXCHNG_TXT)
    expected_text = "Secure File Exchange"
    actual_text = (scr_fl_exchng).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    snd_sfly_drp_zn = driver.find_element(*SND_SFLY_DRP_ZN_TXT)
    expected_text = "SendSafely Dropzone"
    actual_text = (snd_sfly_drp_zn).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    dvlpr_api = driver.find_element(*DVLPR_API_TXT)
    expected_text = "Developer API"
    actual_text = (dvlpr_api).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 3 Click "Pricing" button. Verify "https://www.sendsafely.com/pricing/" is open
    prcng_btn = driver.find_element(*PRCN_BTN)
    prcng_btn.click()
    if driver.current_url == 'https://www.sendsafely.com/pricing/':
        print(f'\nhttps://www.sendsafely.com/pricing/ is here')
    else:
        print(f'\nhttps://www.sendsafely.com/pricing/ is not here')
    driver.back()

    # 4 Click "How it Works" button. Verify "https://www.sendsafely.com/howitworks/" is open
    hw_i_wrks_btn = driver.find_element(*HW_T_WRKS_BTN)
    hw_i_wrks_btn.click()
    if driver.current_url == 'https://www.sendsafely.com/howitworks/':
        print(f'\nhttps://www.sendsafely.com/howitworks/ is here')
    else:
        print(f'\nhttps://www.sendsafely.com/howitworks/ is not here')
    driver.back()

    # 5 Click "Blog" button. Verify "https://blog.sendsafely.com/" is open
    blg_btn = driver.find_element(*BLG_BTN)
    blg_btn.click()
    if driver.current_url == 'https://blog.sendsafely.com/':
        print(f'\nhttps://blog.sendsafely.com/ is here')
    else:
        print(f'\nhttps://blog.sendsafely.com/ is not here')
    driver.back()

    # 6 Click "Log In" button. Verify "https://www.sendsafely.com/auth/" is open
    lgn_btn = driver.find_element(*LGN_BTN)
    lgn_btn.click()
    if driver.current_url == 'https://www.sendsafely.com/auth/':
        print(f'\nhttps://www.sendsafely.com/auth/ is here')
    else:
        print(f'\nhttps://www.sendsafely.com/auth/ is not here')
    driver.back()

    # 7 Click "Request Demo" button. Verify "https://www.sendsafely.com/" is open
    rqst_dm_btn = driver.find_element(*RQST_DM_BTN)
    rqst_dm_btn.click()
    if driver.current_url == 'https://www.sendsafely.com/':
        print(f'\nhttps://www.sendsafely.com/ is here')
    else:
        print(f'\nhttps://www.sendsafely.com/ is not here')
    driver.back()

    sleep(4)
    driver.delete_all_cookies()
    driver.quit()
