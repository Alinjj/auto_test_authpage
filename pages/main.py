#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os,pickle

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or ''

        super().__init__(web_driver, url)
        # with open('my_cookies.txt', 'rb') as cookiesfile:
        #  cookies = pickle.load(cookiesfile)
        #  for cookie in cookies:
        #      web_driver.add_cookie(cookie)
        #  web_driver.refresh();

    # password form
    password = WebElement(id='password')
    # email form
    email = WebElement(id='username')
    #check in on Authpage
    reg = WebElement(id='kc-register')


    #form check in
    first_name = WebElement(name='firstName')
    last_name = WebElement(name='lastName')
    address = WebElement(id='address')
    password_check_in = WebElement(id='password')
    password_check_in_confirm = WebElement(id='password-confirm')
    btn_register = WebElement(name='register')

    #from check in warnings
    first_name_warnings = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    last_name_warnings = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    address_warnings = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/span')
    password_check_in_warnings = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    password_check_in_confirm_warnings = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')

    #form check in next page with auth code
    check_in_email_code = WebElement(xpath='//*[@id="rt-code-0"]')

    # button Войти
    button_enter = WebElement(id='kc-login')
    #products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # icon_email_socialnetworks
    icon_email = WebElement(xpath="//*[@id='oidc_mail']")

    #auth_with_email_social
    Socialemail_email = WebElement(name='Login')
    Socialemail_password = WebElement(name='Password')
    Socialemail_button_enter = WebElement(xpath='//*[@id="login-form"]/div[2]/button')

    #tabs
    tab_phone_number = WebElement(id='t-btn-tab-phone')
    tab_mail = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')

    #placeholders of tabs all the same
    ph_phone = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    ph_mail = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    ph_login = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    ph_ls = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')

    #pingdom check
    url_input = WebElement(id='urlInput')
    start_btn_pingdom = WebElement(xpath='/html/body/app-root/main/app-home-hero/header/section/app-test-runner/div/div[2]/div[3]/input')
    pingdom_values = ManyWebElements(xpath="//div[@class='value']")

    #dropmail.me 10min email for check in tests
    dropmail_email = WebElement(xpath='/html/body/div[2]/div[4]/div/div/div/span[1]')
    #dropmail_code = WebElement(xpath="/html/body/div[@class='container']/div[@class='row'][7]/div[@class='col-12'][2]/ul[@class='list-unstyled messages-list']/li[@class='row no-gutters'][1]/div[@class='col-12']/div[1]/pre")
    dropmail_code = WebElement(xpath='/html/body/div[2]/div[10]/div[2]/ul/li/div[3]/div[1]/pre')
    dropmail_rst_auth_code = WebElement(xpath='/html/body/div[2]/div[10]/div[2]/ul/li[1]/div[3]/div[1]/pre')

    #rst_auth_code_page
    email_input_rst_code_auth = WebElement(xpath='//*[@id="address"]')
    rst_auth_code = WebElement(xpath='//*[@id="rt-code-0"]')
    rst_auth_code_btn_move = WebElement(xpath='//*[@id="page-right"]/div/div/a')
