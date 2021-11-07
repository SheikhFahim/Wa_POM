import sys,time
from selenium.webdriver.common.by import By

class Logout():
    menu='//*[@id="side"]/header/div[2]/div/span/div[3]/div/span'
    logout='/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]'
    def logout(chrome):
        menu = chrome.find_element(By.XPATH, Logout.menu)
        menu.click()  # Finding the Three dot menu and clicking it.
        time.sleep(20)
        logout = chrome.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]')  # Logout process
        logout.click()
