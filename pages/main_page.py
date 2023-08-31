from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

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
FV_ELMNTS_DRPDWN_MNU_HR = (By.XPATH, "//li[@class='nav-item']")
SCR_EML_TXT = (By.XPATH, "(//li[@class='nav-item'])[1]")
HLP_DSK_INTGRTN_TXT = (By.XPATH, "(//li[@class='nav-item'])[2]")
SCR_FL_EXCHNG_TXT = (By.XPATH, "(//li[@class='nav-item'])[3]")
SND_SFLY_DRP_ZN_TXT = (By.XPATH, "(//li[@class='nav-item'])[4]")
DVLPR_API_TXT = (By.XPATH, "(//li[@class='nav-item'])[5]")

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
        sleep(4)
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

    # sendsafely_pytested_bttns_clckd_2
    # 1 Click "Features" button. Verify "https://www.sendsafely.com/features/" is open
    def ftrs_btn(self, ftr_url):
        ftrs_btn = self.driver.find_element(*FTRS_BTN)
        ftrs_btn.click()
        if self.driver.current_url == 'https://www.sendsafely.com/features/':
            print(f'\nhttps://www.sendsafely.com/features/ is here')
        else:
            print(f'\nhttps://www.sendsafely.com/features/ is not here')
        self.driver.back()
    # End of the above code

    # 2 Hover over "Solutions" button. Verify 5 submenu items with texts are here
    def sltns_btn_clck(self):
        sltns_btn_clck = self.driver.find_element(*SLTNS_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(sltns_btn_clck).perform()
        fv_elmnts_drpdwn_mn_hr = self.driver.find_elements(*FV_ELMNTS_DRPDWN_MNU_HR)
        if len(fv_elmnts_drpdwn_mn_hr) == 5:
            print(f'\n5 elements are here')
        else:
            print(f'\nwrong output: {len(fv_elmnts_drpdwn_mn_hr)}')

        scr_eml = self.driver.find_element(*SCR_EML_TXT)
        expected_text = "Secure Email"
        actual_text = (scr_eml).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

        hlp_dsk_intgrtn = self.driver.find_element(*HLP_DSK_INTGRTN_TXT)
        expected_text = "Help Desk Integrations"
        actual_text = (hlp_dsk_intgrtn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

        scr_fl_exchng = self.driver.find_element(*SCR_FL_EXCHNG_TXT)
        expected_text = "Secure File Exchange"
        actual_text = (scr_fl_exchng).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

        snd_sfly_drp_zn = self.driver.find_element(*SND_SFLY_DRP_ZN_TXT)
        expected_text = "SendSafely Dropzone"
        actual_text = (snd_sfly_drp_zn).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

        dvlpr_api = self.driver.find_element(*DVLPR_API_TXT)
        expected_text = "Developer API"
        actual_text = (dvlpr_api).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # End of the above code

    # 3 Click "Pricing" button. Verify "https://www.sendsafely.com/pricing/" is open
    def prcng_btn_clck(self):
        prcng_btn_clck = self.driver.find_element(*PRCN_BTN)
        prcng_btn_clck.click()
        if self.driver.current_url == 'https://www.sendsafely.com/pricing/':
            print(f'\nhttps://www.sendsafely.com/pricing/ is here')
        else:
            print(f'\nhttps://www.sendsafely.com/pricing/ is not here')
        self.driver.back()
    # End of the above code

    # 4 Click "How it Works" button. Verify "https://www.sendsafely.com/howitworks/" is open
    def hw_i_wrks_btn_clck(self):
        hw_i_wrks_btn_clck = self.driver.find_element(*HW_T_WRKS_BTN)
        hw_i_wrks_btn_clck.click()
        if self.driver.current_url == 'https://www.sendsafely.com/howitworks/':
            print(f'\nhttps://www.sendsafely.com/howitworks/ is here')
        else:
            print(f'\nhttps://www.sendsafely.com/howitworks/ is not here')
        self.driver.back()
    # End of the above code

    # 5 Click "Blog" button. Verify "https://blog.sendsafely.com/" is open
    def blg_btn_clck(self):
        blg_btn_clck = self.driver.find_element(*BLG_BTN)
        blg_btn_clck.click()
        if self.driver.current_url == 'https://blog.sendsafely.com/':
            print(f'\nhttps://blog.sendsafely.com/ is here')
        else:
            print(f'\nhttps://blog.sendsafely.com/ is not here')
        self.driver.back()
    # End of the above code

    # 6 Click "Log In" button. Verify "https://www.sendsafely.com/auth/" is open
    def lgn_btn_clck(self):
        lgn_btn_clck = self.driver.find_element(*LGN_BTN)
        lgn_btn_clck.click()
        if self.driver.current_url == 'https://www.sendsafely.com/auth/':
            print(f'\nhttps://www.sendsafely.com/auth/ is here')
        else:
            print(f'\nhttps://www.sendsafely.com/auth/ is not here')
        self.driver.back()
    # End of the above code

    # 7 Click "Request Demo" button. Verify "https://www.sendsafely.com/" is open
    def rqst_dm_btn_clck(self):
        rqst_dm_btn_clck = self.driver.find_element(*RQST_DM_BTN)
        rqst_dm_btn_clck.click()
        if self.driver.current_url == 'https://www.sendsafely.com/':
            print(f'\nhttps://www.sendsafely.com/ is here')
        else:
            print(f'\nhttps://www.sendsafely.com/ is not here')
        self.driver.back()

    # End of the above code
