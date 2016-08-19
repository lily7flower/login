#-*- coding:UTF-8 -*-
import os
import time
from selenium import webdriver

chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver_x64.exe'
os.environ['webdriver.chrome.driver'] = chromedriver
def login(url,name,pwd):
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    driver.maximize_window() # 将浏览器最大化显示
    time.sleep(2) # 控制间隔时间，等待浏览器反映
    driver.find_element_by_id("id").send_keys(name)  #需要根据实际登录的网页查找具体id
    driver.find_element_by_id("pwd").send_keys(pwd) 
    driver.find_element_by_id("b_login").click()

def main():
    url = ' '
    name = ' '
    pwd = ' '   
    login(url,name,pwd)

if __name__ == '__main__':
    main()
