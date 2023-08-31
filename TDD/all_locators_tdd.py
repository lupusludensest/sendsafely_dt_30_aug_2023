from selenium.webdriver.common.by import By


# Locators
SND_SFL_PCTR = (By.XPATH, "//img[@src='/img/ss_logo_60_343.png']") # (By.XPATH, "//img[@alt='logo']")
GLB_S_SCHM_PCTR = (By.XPATH, "//img[@src='/img/globe_lines.png']")
E2E_TXT_ECRPTN_TXT = (By.XPATH, "//h1[@class='f_700 f_size_40 l_height50 w_color mb_20 wow fadeInRight']")
ACPT_CCKS_BTN = (By.ID, "cookie_accept")
FTRS_BTN = (By.XPATH, "(//a[@href='/features/'])[1]")  # (By.XPATH, "//a[normalize-space()='Features']")
SLTNS_BTN = (By.XPATH, "//a[@class='dropdown-toggle nav-link']")  # (By.XPATH, "//a[@title='Solutions']")
FV_ELMNTS_DRPDWN_MNU_HR = (By.XPATH, "//li[@class='nav-item']")
SCR_EML_TXT = (By.XPATH, "(//li[@class='nav-item'])[1]")
HLP_DSK_INTGRTN_TXT = (By.XPATH, "(//li[@class='nav-item'])[2]")
SCR_FL_EXCHNG_TXT = (By.XPATH, "(//li[@class='nav-item'])[3]")
SND_SFLY_DRP_ZN_TXT = (By.XPATH, "(//li[@class='nav-item'])[4]")
DVLPR_API_TXT = (By.XPATH, "(//li[@class='nav-item'])[5]")
PRCN_BTN = (By.XPATH, "//a[@href='/pricing/']")  # (By.XPATH, "//a[normalize-space()='Pricing']")
HW_T_WRKS_BTN = (By.XPATH, "//a[@href='/howitworks/']")  # (By.XPATH, "//a[@class='nobr nav-link']")
BLG_BTN = (By.XPATH, "//a[@href='https://blog.sendsafely.com']")  # (By.XPATH, "//a[normalize-space()='Blog']")
LGN_BTN = (By.XPATH, "//a[@href='/auth/']")
RQST_DM_BTN = (By.XPATH, "//nobr[normalize-space()='Request Demo']")
SGN_P_BTN = (By.XPATH, "//section[@class='agency_banner_area_two']//a[1]")
LRN_MR_BTN = (By.XPATH, "//a[@id='intro-button']//div[@class='btn btn-lg btn-orange'][normalize-space()='Learn More']")