from pages.all_locators_bdd import *
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import string

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

    # Sign up by randomized email. Verify "https://www.sendsafely.com/auth/#signup" is open.
    # 1 Click button "Sign up Now"
    def clck_sgb_p_btn(self):
        self.driver.find_element(*SGN_P_BTN).click()
    # End of the above code

    # 2 Enter the email randomized to "Email address" empty field
    def ntr_rndmzd_eml_t_clnsd_emty_fld(self):
        def generate_random_email():
            domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            email = f"{username}@{domain}"
            return email

        # Generate random email, login, and password
        random_email = generate_random_email()

        print(f"\nRandom Email: {random_email}")

        # Send randomly generated email to cleansed and empty email field
        empty_email_field = self.driver.find_element(*EML_ADDRSS_FLD)
        empty_email_field.clear()
        empty_email_field.send_keys(random_email)
    # End of the above code

    # 3 Click on "Get Started" button
    def clck_n_gt_strd_btn(self):
        self.driver.find_element(*GT_STRTD_BTN).click()
    # End of the above code

    # 4 Verify "https://www.sendsafely.com/auth/#signup" is open
    def vtf_sgn_p_url_pn(self):
        self.driver.find_element(*GT_STRTD_BTN)
        if self.driver.current_url == 'https://www.sendsafely.com/auth/#signup':
            print(f'\nhttps://www.sendsafely.com/auth/#signup is here')
        else:
            print(f'\nhttps://www.sendsafely.com/auth/#signup is not here')
        self.driver.back()
    # End of the above code
