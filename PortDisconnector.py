from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from xvfbwrapper import Xvfb
from selenium.common.exceptions import NoSuchElementException
import threading

password = 'Put password here'
valueList = ['1048614','38','1048611','35','32']
phantomjs_path = 'C:/Python27/Scripts/phantomjs.exe'
index = 0
xpath = '//*[@id="pagepost"]/table[1]/tbody/tr[2]/td[2]/select'


#browser = webdriver.Firefox()
browser = webdriver.PhantomJS(phantomjs_path)
browser.set_window_size(1400, 1000)
browser.get('http://192.168.1.254/xslt?PAGE=C_2_2')
def worker():
    inputStr = ''
    inputStr = raw_input("Type 'q' to quit\n")
    while inputStr != 'q':
        inputStr = raw_input("Type 'q' to quit\n")
    return
t = threading.Thread(target=worker)
t.start()
while t.isAlive():
    try:
        element = browser.find_element_by_name('ADM_PASSWORD')
        element.clear()
        element.send_keys(password)
        element.submit()
    except NoSuchElementException:
        element = browser.find_element_by_xpath(xpath)
        select = Select(element)
        if index > (len(valueList) - 1):
            index = 0
        select.select_by_value(valueList[index])
        index += 1
        element.submit()
try:
    element = browser.find_element_by_name('ADM_PASSWORD')
    element.clear()
    element.send_keys(password)
    element.submit()
    element = browser.find_element_by_xpath(xpath)
    select = Select(element)
    select.select_by_value('32')
    element.submit()
except NoSuchElementException:
    element = browser.find_element_by_xpath(xpath)
    select = Select(element)
    select.select_by_value('32')
    element.submit()

browser.close()
