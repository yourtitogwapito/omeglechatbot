# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:25:35 2023

@author: P102MNPH1
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("http://omegle.com")


cl_interest = "newtopicinput"
interest = driver.find_element(By.CLASS_NAME, cl_interest)
interest.send_keys("Valorant")

id_text = "textbtn"
driver.find_element(By.ID,id_text).click()

chkBox1 = "/html/body/div[7]/div/p[1]/label/input"
driver.find_element(By.XPATH, chkBox1).click()

chkBox2 = "/html/body/div[7]/div/p[2]/label/input"
driver.find_element(By.XPATH, chkBox2).click()

btn_Confirm = "/html/body/div[7]/div/p[3]/input"
driver.find_element(By.XPATH, btn_Confirm).click()


#================================

chatarea = "chatmsg"
btn_send = "sendbtn"
btn_escEnter = "disconnectbtn"

"""
Case 1
*first to chat
"""

while True:
    try:
        time.sleep(3)
        txtBx_chatarea = driver.find_element(By.CLASS_NAME, chatarea) #look for chatarea
        txtBx_chatarea.send_keys("Hi")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, btn_send).click() #send message
        escEnter = driver.find_element(By.CLASS_NAME, btn_escEnter) #look for esc btn
        escEnter.click()
        escEnter.click()
        escEnter.click()
        
    except ElementNotInteractableException:
        time.sleep(3)
        escEnter = driver.find_element(By.CLASS_NAME, btn_escEnter) #look for esc btn
        escEnter.click()
        txtBx_chatarea = driver.find_element(By.CLASS_NAME, chatarea) #look for chatarea
        txtBx_chatarea.send_keys("Hi")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, btn_send).click() #send message
        escEnter = driver.find_element(By.CLASS_NAME, btn_escEnter) #look for esc btn
        escEnter.click()
        escEnter.click()
        escEnter.click()
    
    except KeyboardInterrupt:
        print("keyboard interruption")
        driver.quit()
        raise SystemExit
        
    
        



        



























