import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.infostock.co.kr/bord.asp'

dict = {"init" : "init"}
skwords = {"특징 종목(코스닥)", "특징 종목(코스피)", "특징 상한가"}

driver = webdriver.Edge(executable_path=r"C:\Users\kitty\Documents\Template\prac2\msedgedriver")
driver.get(url=URL)
control = driver.find_element_by_xpath("""//*[@id="StartDate"]""")
control.send_keys("2021-06-15")
control = driver.find_element_by_xpath("""//*[@id="EndDate"]""")
control.send_keys("2021-06-15")
control = driver.find_element_by_xpath("""//*[@id="market_2"]/article/table/tbody[1]/tr/td/table/tbody/tr/td/form/div[2]/input""")
#control.send_keys("특징 종목(코스닥)")
#control.send_keys("특징 종목(코스피)")
control.send_keys("특징 상한가")
control = driver.find_element_by_xpath("""//*[@id="market_2"]/article/table/tbody[1]/tr/td/table/tbody/tr/td/form/div[2]/button""")
control.click()

control = driver.find_elements_by_class_name("tr_")[1]
a_control = control.find_elements_by_tag_name("a")

for con in a_control :
    link = con.get_attribute('href')
    if(link != None) : 
        con.click()
        break

control = driver.find_element_by_class_name("tbl")
tr_controls = control.find_elements_by_tag_name("tr")

for tr_control in tr_controls:
    str = tr_control.text
    if("%" in str):
        txtarr = str.split('\n')
        dict[txtarr[0]] = txtarr[3]

f = open("새파일.txt:", 'w')
f.close()
