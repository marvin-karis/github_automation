import sys
import requests
import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller

keyboard = Controller()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options ,executable_path='../webdriver2/chromedriver.exe')
driver.get("https://github.com/login")

inputElement = driver. find_element_by_xpath("//*[@id='login_field']")
inputElement.send_keys('---INPUT USERNAME---')
inputElement = driver. find_element_by_xpath("//*[@id='password']")
inputElement.send_keys('---INPUT PASSWORD---')
inputElement = driver. find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]")
inputElement.submit()
driver.get("https://github.com/new/")
inputElement = driver.find_element_by_xpath("//*[@id='repository_name']")
repository_name = input("")
inputElement.send_keys(repository_name)

webelement_checkbox = driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/div[1]")
webelement_checkbox.click()
#if webelement_checkbox.click() is True:
 #   print("public checkbox clicked")
#else:
 #   print("path not found")
InputElement = driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button")
InputElement.submit()
