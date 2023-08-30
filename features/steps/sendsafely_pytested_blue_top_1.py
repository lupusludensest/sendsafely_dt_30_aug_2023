from behave import *


@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then('Click button "Accept" cookies')
def accpt_ccks_btn(context):
    """
    Click button "Accept" cookies
    """
    context.app.main_page.accpt_ccks_btn()


@then("1 Picture SENDSAFELY '{snd_sfl_pctr_name}' is present")
def snd_sfl_pctr(context, snd_sfl_pctr_name):
    """
    1 Picture SENDSAFELY '/img/ss_logo_60_343.png' is present
    """
    context.app.main_page.snd_sfl_pctr(snd_sfl_pctr_name)


@then("2 Picture Globe as a Schema '{glb_s_schm_pctr_name}' is present")
def glb_s_schm_pctr(context, glb_s_schm_pctr_name):
    """
    2 Picture Globe as a Schema '/img/globe_lines.png' is present
    """
    context.app.main_page.glb_s_schm_pctr(glb_s_schm_pctr_name)


@then('3 Text "{e2e_txt_encrptn_txt_name}" is here')
def e2e_txt_encrptn_txt(context, e2e_txt_encrptn_txt_name):
    """
    3 Text "The end-to-end encryption platform for modern business" is here
    """
    context.app.main_page.e2e_txt_encrptn_txt(e2e_txt_encrptn_txt_name)


@then('4 "{ftrs_btn_txt}" button is here')
def ftrs_btn(context, ftrs_btn_txt):
    """
    4 "Features" button is here
    """
    context.app.main_page.ftrs_btn(ftrs_btn_txt)


@then('5 "{sltns_btn_txt}" button is here')
def sltns_btn(context, sltns_btn_txt):
    """
    5 "Solutions" button is here
    """
    context.app.main_page.sltns_btn(sltns_btn_txt)


@then('6 "{prcng_btn_txt}" button is here')
def prcng_btnl(context, prcng_btn_txt):
    """
    6 "Pricing" button is here
    """
    context.app.main_page.prcng_btn(prcng_btn_txt)


@then('7 "{hw_t_wrks_btn_txt}" button is here')
def hw_t_wrks_btn(context, hw_t_wrks_btn_txt):
    """
    7 "How It Works" button is here
    """
    context.app.main_page.hw_t_wrks_btn(hw_t_wrks_btn_txt)


@then('8 "{blg_btn_txt}" button is here')
def blg_btn(context, blg_btn_txt):
    """
    8 "Blog" button is here
    """
    context.app.main_page.blg_btn(blg_btn_txt)


@then('9 "{lgn_btn_txt}" button is here')
def lgn_btn(context, lgn_btn_txt):
    """
    9 "Log In" button is here
    """
    context.app.main_page.lgn_btn(lgn_btn_txt)


@then('10 "{rqst_dm_btn_txt}" button is here')
def rqst_dm_btn(context, rqst_dm_btn_txt):
    """
    10 "Request Demo" button is here
    """
    context.app.main_page.rqst_dm_btn(rqst_dm_btn_txt)


@then('11 "{sgn_p_btn_txt}" button is here')
def sgn_p_btn(context, sgn_p_btn_txt):
    """
    11 "Sign up Now" button is here
    """
    context.app.main_page.sgn_p_btn(sgn_p_btn_txt)


@step('12 "{lrn_mr_btn_txt}" button is here')
def lrn_mr_btn(context, lrn_mr_btn_txt):
    """
    12 "Learn More " button is here
    """
    context.app.main_page.lrn_mr_btn(lrn_mr_btn_txt)