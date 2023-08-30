from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Locators
SND_SFL_PCTR = (By.XPATH, "//img[@src='/img/ss_logo_60_343.png']") # (By.XPATH, "//img[@alt='logo']")
GLB_S_SCHM_PCTR = (By.XPATH, "//img[@src='/img/globe_lines.png']")
ACPT_CCKS_BTN = (By.ID, "cookie_accept")
E2E_TXT_ECRPTN_TXT = (By.XPATH, "//h1[@class='f_700 f_size_40 l_height50 w_color mb_20 wow fadeInRight']")
FTRS_BTN = (By.XPATH, "(//a[@href='/features/'])[1]") # (By.XPATH, "//a[normalize-space()='Features']")
SLTNS_BTN = (By.XPATH, "//a[@class='dropdown-toggle nav-link']") # (By.XPATH, "//a[@title='Solutions']")
PRCN_BTN = (By.XPATH, "//a[@href='/pricing/']") # (By.XPATH, "//a[normalize-space()='Pricing']")
HW_T_WRKS_BTN = (By.XPATH, "//a[@href='/howitworks/']") # (By.XPATH, "//a[@class='nobr nav-link']")
BLG_BTN = (By.XPATH, "//a[@href='https://blog.sendsafely.com']") # (By.XPATH, "//a[normalize-space()='Blog']")
LGN_BTN = (By.XPATH, "//a[@href='/auth/']")
RQST_DM_BTN = (By.XPATH, "//nobr[normalize-space()='Request Demo']")
SGN_P_BTN = (By.XPATH, "//section[@class='agency_banner_area_two']//a[1]")
LRN_MR_BTN = (By.XPATH, "//a[@id='intro-button']//div[@class='btn btn-lg btn-orange'][normalize-space()='Learn More']")

class MainPage(Page):

    # test_sendsafely_pytested_blue_top_1
    # Click button "Accept" cookies
    def accpt_ccks_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(ACPT_CCKS_BTN)).click()
    # End of the above code

    # 1 Picture SENDSAFELY '/img/ss_logo_60_343.png' is present
    def snd_sfl_pctr(self, snd_sfl_pctr_name):
        snd_sfl_pctr = self.wait.until(EC.visibility_of_element_located(SND_SFL_PCTR))  # driver.find_element(*SND_SFL_PSTR)
        if snd_sfl_pctr_name in snd_sfl_pctr.get_attribute('src'):
            print(f'\nImage SENDSAFELY is visible on screen')
        else:
            print(f'\nImage SENDSAFELY is not visible on screen')
    # End of the above code

    # 2 Picture Globe as a Schema '/img/globe_lines.png' is present
    def glb_s_schm_pctr(self, glb_s_schm_pctr_name):
        glb_s_schm_pctr = self.wait.until(EC.visibility_of_element_located(GLB_S_SCHM_PCTR))
        if glb_s_schm_pctr_name in glb_s_schm_pctr.get_attribute('src'):
            print(f'\nImage Globe as a Schema is visible on screen')
        else:
            print(f'\nImage Globe as a Schema is not visible on screen')
    # End of the above code

    # 3 Text "The end-to-end encryption platform for modern business" is here
    def e2e_txt_encrptn_txt(self, e2e_txt_encrptn_txt_name):
        e2e_txt_encrptn_txt = self.driver.find_element(*E2E_TXT_ECRPTN_TXT)
        expected_text = e2e_txt_encrptn_txt_name
        actual_text = (e2e_txt_encrptn_txt).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 4 "Features" button is here
    def ftrs_btn(self, ftrs_btn_txt):
        ftrs_btn = self.driver.find_element(*FTRS_BTN)
        expected_text = ftrs_btn_txt
        actual_text = (ftrs_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 5 "Solutions" button is here
    def sltns_btn(self, sltns_btn_txt):
        sltns_btn = self.driver.find_element(*SLTNS_BTN)
        expected_text = sltns_btn_txt
        actual_text = (sltns_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 6 "Pricing" button is here
    def prcng_btn(self, prcng_btn_txt):
        prcng_btn = self.driver.find_element(*PRCN_BTN)
        expected_text = prcng_btn_txt
        actual_text = (prcng_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 7 "How It Works" button is here
    def hw_t_wrks_btn(self, hw_t_wrks_btn_txt):
        hw_t_wrks_btn = self.driver.find_element(*HW_T_WRKS_BTN)
        expected_text = hw_t_wrks_btn_txt
        actual_text = (hw_t_wrks_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 8 "Blog" button is here
    def blg_btn(self, blg_btn_txt):
        blg_btn = self.driver.find_element(*BLG_BTN)
        expected_text = blg_btn_txt
        actual_text = (blg_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 9 "Log In" button is here
    def lgn_btn(self, lgn_btn_txt):
        lgn_btn = self.driver.find_element(*LGN_BTN)
        expected_text = lgn_btn_txt
        actual_text = (lgn_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 10 "Request Demo" button is here
    def rqst_dm_btn(self, rqst_dm_btn_txt):
        rqst_dm_btn = self.driver.find_element(*RQST_DM_BTN)
        expected_text = rqst_dm_btn_txt
        actual_text = (rqst_dm_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 11 "Sign up Now" button is here
    def sgn_p_btn(self, sgn_p_btn_txt):
        sgn_p_btn = self.driver.find_element(*SGN_P_BTN)
        expected_text = sgn_p_btn_txt
        actual_text = (sgn_p_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 12 "Learn More " button is here
    def lrn_mr_btn(self, lrn_mr_btn_txt):
        lrn_mr_btn = self.driver.find_element(*LRN_MR_BTN)
        expected_text = lrn_mr_btn_txt
        actual_text = (lrn_mr_btn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code