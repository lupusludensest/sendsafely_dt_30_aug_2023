from behave import *

use_step_matcher("re")


@then('1 Click button "Sign up Now"')
def clck_sgb_p_btn(context):
    """
    1 Click button "Sign up Now"
    """
    context.app.main_page.clck_sgb_p_btn()


@then('2 Enter the email randomized to "Email address" empty field')
def ntr_rndmzd_eml_t_clnsd_emty_fld(context):
    """
    2 Enter the email randomized to "Email address" empty field
    """
    context.app.main_page.ntr_rndmzd_eml_t_clnsd_emty_fld()

@step('3 Click on "Get Started" button')
def clck_n_gt_strd_btn(context):
    """
    3 Click on "Get Started" button
    """
    context.app.main_page.clck_n_gt_strd_btn()

@step('4 Verify "https://www.sendsafely.com/auth/#signup" is open')
def vtf_sgn_p_url_pn(context):
    """
    4 Verify "https://www.sendsafely.com/auth/#signup" is open
    """
    context.app.main_page.vtf_sgn_p_url_pn()