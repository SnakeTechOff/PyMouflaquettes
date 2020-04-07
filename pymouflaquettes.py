#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-. iso-8859-1

###### Import ########

import sys
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from time import sleep

###### Variable ######

folder = "./geckodriver/"
exec_path = folder + "geckodriver.exe"
log_file = folder + "geckodriver.log"

url = "https://www.tremplin-musical.com/connexion"
mouflaquettes = "https://www.tremplin-musical.com/candidatures/2153"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"

###### Function ######


###### Program #######

if __name__ == "__main__":
    with open('secret.json') as json_data:
        data = json.load(json_data)
        email = data['email']
        password = data['password']
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent)
    browser = webdriver.Firefox(profile,executable_path=exec_path, service_log_path=log_file)
    browser.get(url)
    sleep(2)
    browser.find_element_by_xpath("/html/body/div[4]/div/div/div/a[1]").click()
    sleep(2)
    browser.find_element_by_id("user_account_email").send_keys(email)
    browser.find_element_by_id("user_account_password").send_keys(password)
    browser.find_element_by_name("commit").click()
    sleep(2)
    browser.get(mouflaquettes)
    sleep(2)
    try:
        browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div/form[1]/button/span[2]").click()
    except:
        print("[+] Vote du jour déjà effectué")
    sleep(2)
    browser.close()
    sys.exit(0)