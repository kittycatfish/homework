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

date = "2021-06-15"

driver = webdriver.Edge(executable_path=r"C:\Users\kitty\Documents\Template\prac2\homework\msedgedriver")

for kw in skwords:
    driver.get(url=URL)
    control = driver.find_element_by_xpath("""//*[@id="StartDate"]""")
    control.send_keys(date)
    control = driver.find_element_by_xpath("""//*[@id="EndDate"]""")
    control.send_keys(date)
    control = driver.find_element_by_xpath("""//*[@id="market_2"]/article/table/tbody[1]/tr/td/table/tbody/tr/td/form/div[2]/input""")
    control.send_keys(kw)
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
        if("%)" in str):
            txtarr = str.split('\n')
            if(len(txtarr) < 4): continue
            if(txtarr[0] not in dict):
                dict[txtarr[0]] = txtarr[3]

filename = date + ".txt"
f = open(filename, 'w')

for data in dict :
    str = data + '\t' + dict[data] + '\n'
    f.write(str)

f.close()
