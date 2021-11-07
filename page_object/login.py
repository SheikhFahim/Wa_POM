import sys,time
from selenium.webdriver.common.by import By

class Login():
    search='//*[@id="side"]/div[1]/div/label/div/div[2]'

    def page_search(chrome,n):
        s_box = chrome.find_element(By.XPATH, Login.search)  # Finding search box to search number
        s_box.click()
        time.sleep(5)
        s_box.send_keys(n)                        # Inputing the number from the xlsx file
        time.sleep(6)

