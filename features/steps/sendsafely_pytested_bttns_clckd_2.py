from behave import *

@then('1 Click "Features" button. Verify "{ftr_url}" is open')
def ftrs_btn(context, ftr_url):
    """
    1 Click "Features" button. Verify "https://www.sendsafely.com/features/" is open
    """
    context.app.main_page.ftrs_btn(ftr_url)


@then('2 Hover over "Solutions" button. Verify 5 submenu items with texts are here')
def sltns_btn_clck(context):
    """
    2 Hover over "Solutions" button. Verify 5 submenu items with texts are here
    """
    context.app.main_page.sltns_btn_clck()


@then('3 Click "Pricing" button. Verify "https://www.sendsafely.com/pricing/" is open')
def prcng_btn_clck(context):
    """
    3 Click "Pricing" button. Verify "https://www.sendsafely.com/pricing/" is open
    """
    context.app.main_page.prcng_btn_clck()


@then('4 Click "How it Works" button. Verify "https://www.sendsafely.com/howitworks/" is open')
def hw_i_wrks_btn_clck(context):
    """
    4 Click "How it Works" button. Verify "https://www.sendsafely.com/howitworks/" is open
    """
    context.app.main_page.hw_i_wrks_btn_clck()


@then('5 Click "Blog" button. Verify "https://blog.sendsafely.com/" is open')
def blg_btn_clck(context):
    """
    5 Click "Blog" button. Verify "https://blog.sendsafely.com/" is open
    """
    context.app.main_page.blg_btn_clck()


@then('6 Click "Log In" button. Verify "https://www.sendsafely.com/auth/" is open')
def lgn_btn_clck(context):
    """
    6 Click "Log In" button. Verify "https://www.sendsafely.com/auth/" is open
    """
    context.app.main_page.lgn_btn_clck()


@step('7 Click "Request Demo" button. Verify "https://www.sendsafely.com/" is open')
def rqst_dm_btn_clck(context):
    """
    7 Click "Request Demo" button. Verify "https://www.sendsafely.com/" is open
    """
    context.app.main_page.rqst_dm_btn_clck()