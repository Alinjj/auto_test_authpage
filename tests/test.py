#!/usr/bin/python3
# -*- encoding=utf8 -*-
from env import AuthData
import requests
#import time, pickle
import pytest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.main import MainPage
from pages.elements import ManyWebElements
from selenium.webdriver.common.action_chains import ActionChains
import time
import names
import random

def test_rostelecom_is_ok(web_browser):
    """ Site opens _status code is 200 """
    page = MainPage(web_browser)
    r = requests.get("")
    if r.status_code == 200 and page._web_driver.current_url == "":
        page._web_driver.save_screenshot('auth_is_ok_1_test.png')
    page._web_driver.quit()

def test_auth_successful_email(web_browser):
    """ Successful auth with valid Data """
    try:
        page = MainPage(web_browser)
        page.password.send_keys(AuthData.PASSWORD_rst)
        page.email.send_keys(AuthData.EMAIL)
        page.button_enter.click()
    except:
        raise Exception('Login Error')
    finally:
        page._web_driver.quit()
def test_auth_successful_login(web_browser):
    """ Successful auth with valid Data """
    try:
        page = MainPage(web_browser)
        page.password.send_keys(AuthData.PASSWORD_rst)
        page.tab_login.send_keys(AuthData.LOGIN)
        page.button_enter.click()
    except:
        raise Exception('Login Error')
    finally:
        page._web_driver.quit()

def test_auth_successful_ls(web_browser):
    """ Successful auth with valid Data """
    try:
        page = MainPage(web_browser)
        page.password.send_keys(AuthData.PASSWORD_rst)
        page.tab_login.send_keys(AuthData.LS)
        page.button_enter.click()
    except:
        raise Exception('Login Error')
    finally:
        page._web_driver.quit()

def test_auth_unsuccessful_invalid_data(web_browser):
    """ UNSuccessful auth with invalid Data """
    try:
        page = MainPage(web_browser)
        page.password.send_keys()
        page.email.send_keys()
        page.button_enter.click()
        raise Exception('Invalid data')
    except Exception as error:
        if page._web_driver.current_url != "":
            print("Exception exception" + str(error))
        page._web_driver.quit()

def test_auth_with_socialnetworks(web_browser):
    """ Auth with socialNetworks Email"""
    page = MainPage(web_browser)
    page.icon_email.click()
    page.Socialemail_email.send_keys(AuthData.SOCIALEMAIL_EMAIL)
    page.Socialemail_password.send_keys(AuthData.SOCIALEMAIL_PASSWORD)
    page.Socialemail_button_enter.click()
    page._web_driver.quit()


def test_placeholder_change_with_tab(web_browser):
    """ Change plaholders when tabs changed """
    page = MainPage(web_browser)

    stat_ph_phone = page.ph_phone.get_attribute('textContent')
    mb_ph = 'Мобильный телефон'


    page.tab_mail.click()
    stat_ph_mail = page.ph_mail.get_attribute('textContent')
    mb_em = 'Электронная почта'

    page.tab_login.click()
    stat_ph_login = page.ph_login.get_attribute('textContent')
    mb_lg = page.tab_login.get_attribute('textContent')

    page.tab_ls.click()
    stat_ph_ls = page.ph_ls.get_attribute('textContent')
    mb_ls = page.tab_ls.get_attribute('textContent')
    ph_list = [stat_ph_ls,stat_ph_login,stat_ph_mail,stat_ph_phone]
    mb_list = [mb_ls,mb_lg,mb_em,mb_ph]
    assert len(ph_list) == len(mb_list)


    page._web_driver.quit()

def test_speed_rst(web_browser):
    """Performance grade,Load time,Page size,Requests"""
    global values, page
    try:
        page = MainPage(web_browser,url='https://tools.pingdom.com/#616085816c400000')
        #page._web_driver.get('https://tools.pingdom.com/#616085816c400000')
        values = page.pingdom_values.get_attribute('textContent')
        page.url_input.send_keys('')
        page.start_btn_pingdom.click()
        values_now = page.pingdom_values.get_attribute('textContent')
        assert int(values_now[0]) >= 95
        #keys = ['performance grade', 'Page size', 'Load time', 'Requests']
        #array = dict(zip(keys, values_now))
        raise Exception('Loading Error')

    except Exception as error:
        print("Exception exception" + str(error))
    finally:
        assert int(values[0]) >= 95
        #keys = ['performance grade', 'Page size', 'Load time', 'Requests']
        #array = dict(zip(keys, values))
        #print(array)
        page._web_driver.quit()

    try:
        page = MainPage(web_browser)
        page._web_driver.get('https://tools.pingdom.com/#616085816c400000')
        values = page.pingdom_values.get_attribute('textContent')
        page._web_driver.save_screenshot('Performance grade_load_size_req.png')
        # Average Good Rating
        assert int(values[0]) >= 95
        keys = ['performance grade','Page size','Load time','Requests' ]
        array = dict(zip(keys,values))
        print(array)
    finally:
        page._web_driver.quit()

def test_checkin_valid_invalid_data(web_browser):
   """check in with invalid/valid data(random data)"""

   page = MainPage(web_browser)
   page.reg.click()
   current_url = page._web_driver.current_url
   page.password_check_in.random_password()
   page.password_check_in_confirm.random_password()
   page.first_name.random_firsName()
   page.last_name.random_lastName()
   page.address.send_keys(AuthData.EMAIL)
   page.btn_register.click()
   if page._web_driver.current_url != current_url:
       raise Exception('Server error, you"r not on check in page')
   page._web_driver.quit()

def test_check_in(web_browser):
    """check in with valid data"""
#######  CHANGE AuthData * for valid data ######
    page = MainPage(web_browser)
    try:
        page = MainPage(web_browser)
        page.reg.click()
        current_url = page._web_driver.current_url
        page.password_check_in.send_keys(AuthData.PASSWORD_rst)
        page.password_check_in_confirm.send_keys(AuthData.PASSWORD_rst)
        page.first_name.send_keys(AuthData.EMAIL)
        page.last_name.send_keys(AuthData.EMAIL)
        page.address.send_keys(AuthData.EMAIL)
        page.btn_register.click()
        if page._web_driver.current_url == current_url:
            raise Exception('Check in error;Data invalid or Server error')
    finally:
        page._web_driver.quit()

def test_change_user_agent(web_browser):
    """Change user agent from abroad"""

    page = MainPage(web_browser,url='https://www.whatismybrowser.com/detect/what-is-my-user-agent/')
    user_agent = page._web_driver.execute_script("return navigator.userAgent")
    page.change_user_agent()
    agent = page._web_driver.execute_script("return navigator.userAgent")


    assert user_agent != agent
    page._web_driver.quit()

def test_log_in_with_user_agent(web_browser):
   """Use user-agent from abroad for log in """

    page = MainPage(web_browser)
    page.change_user_agent()

    page.password.send_keys(AuthData.PASSWORD_rst)
    page.email.send_keys(AuthData.EMAIL)
    page.button_enter.click()

    assert page._web_driver.current_url != ''
    page._web_driver.quit()

def test_check_in_with_code_use10minemail(web_browser):
    """Use a valid 10min email for succesfull auth tests(anonymous check in)There are some JS Fully autonomy registration"""

    page = MainPage(web_browser)
    #page.change_user_agent()


    window_before = page._web_driver.window_handles[0]


    page._web_driver.execute_script("window.open('https://dropmail.me/ru/')")
    #time.sleep(10)
    window_after = page._web_driver.window_handles[1]
    page._web_driver.switch_to.window(window_after)
    #time.sleep(10)
    email = page.dropmail_email.get_attribute('textContent')


    page._web_driver.switch_to.window(window_before)
    page.reg.click()
    page.first_name.random_russian_first_name()
    page.last_name.random_russian_first_name()
    page.address.send_keys(email)
    page.password_check_in.send_keys(AuthData.PASSWORD_rst)
    page.password_check_in_confirm.send_keys(AuthData.PASSWORD_rst)
    page.btn_register.click()

    page._web_driver.switch_to.window(window_after)
    #time.sleep(20)
    code = page.dropmail_code.get_attribute('innerHTML').split()
    #time.sleep(15)
    page._web_driver.switch_to.window(window_before)
    page.check_in_email_code.click()
    page.check_in_email_code.send_keys(code[3])
    #time.sleep(5)



    page._web_driver.quit()


def test_auth_with_rst_code(web_browser):
"""Auth with valid data and auth_rst code"""
    page = MainPage(web_browser)
    #page.change_user_agent()


    window_before = page._web_driver.window_handles[0]


    page._web_driver.execute_script("window.open('https://dropmail.me/ru/')")
    #time.sleep(10)
    window_after = page._web_driver.window_handles[1]
    page._web_driver.switch_to.window(window_after)
    #time.sleep(10)
    email = page.dropmail_email.get_attribute('textContent')


    page._web_driver.switch_to.window(window_before)
    page.reg.click()
    page.first_name.random_russian_first_name()
    page.last_name.random_russian_first_name()
    page.address.send_keys(email)
    page.password_check_in.send_keys(AuthData.PASSWORD_rst)
    page.password_check_in_confirm.send_keys(AuthData.PASSWORD_rst)
    page.btn_register.click()

    page._web_driver.switch_to.window(window_after)
    #time.sleep(20)
    code = page.dropmail_code.get_attribute('innerHTML').split()
    #time.sleep(15)
    page._web_driver.switch_to.window(window_before)
    page.check_in_email_code.click()
    page.check_in_email_code.send_keys(code[3])
    #time.sleep(5)

    page._web_driver.execute_script("window.open('')")
    window_rst_code_auth = page._web_driver.window_handles[2]
    page._web_driver.switch_to.window(window_rst_code_auth)
    #page.email_input_rst_code_auth.send_keys(email)

    page._web_driver.switch_to.window(window_after)
    #time.sleep(15)
    auth_code_rst = page.dropmail_rst_auth_code.get_attribute('innerHTML').split()

    page._web_driver.switch_to.window(window_rst_code_auth)
    # page.rst_auth_code.send_keys(auth_code_rst[3])
    page.rst_auth_code_btn_move.click()
    assert page._web_driver.current_url != ('')

    page._web_driver.quit()


def test_invalid_enter_stress(web_browser):
"""Checking for repetition of invalid data filled fields"""
    page = MainPage(web_browser)

    #page.change_user_agent()
    try:
        for i in range(10):
            page.email.send_keys(AuthData.EMAIL)
            page.password.send_keys(AuthData.PASSWORD_rst)
            page.button_enter.click()
        assert page._web_driver.current_url == 'MAIN_URL'
        raise Exception('Request denied')
    except Exception as error:
        print("Exception exception" + str(error))
    finally:
        page._web_driver.quit()


def test_check_in_form_warnings(web_browser):
 """Checking warnings placaholedrs of check in form"""
    page = MainPage(web_browser)
    page.reg.click()

    page.btn_register.click()

    if page.first_name_warnings.is_visible():
        if page.first_name_warnings.is_visible():
            page.first_name.random_russian_first_name()
            page.btn_register.click()
        else:
            raise Exception('firstName error')
        if page.last_name_warnings.is_visible():
            page.last_name.random_russian_last_name()
            page.btn_register.click()
        else:
            raise Exception('lastName error')
        if page.address_warnings.is_visible():
            page.address.send_keys(AuthData.EMAIL)
            page.btn_register.click()
        else:
            raise Exception('address error')
        if page.password_check_in_warnings.is_visible():
            page.password_check_in.send_keys(AuthData.PASSWORD_rst)
            page.password_check_in_confirm.send_keys(AuthData.PASSWORD_rst)
            page.btn_register.click()
            after_url = page._web_driver.current_url
        else:
            raise Exception('address error')

        assert after_url != page._web_driver.current_url
    else:
        raise Exception('account already exists')

    time.sleep(2)

    page._web_driver.quit()















    



























