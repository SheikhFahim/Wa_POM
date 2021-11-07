import sys,time
import xlsxwriter
from selenium.webdriver.common.by import By


class Send():
    cle='//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span'
    tbox= '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
    send_button='//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button/span'
    status='//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]/div[1]'
    d = "Delivered"
    def send_message(chrome,message):
        userclick = chrome.find_element(By.XPATH,Send.cle)
        userclick.click()
        time.sleep(15)
        t_box = chrome.find_element(By.XPATH,Send.tbox)                        # Text box Operation
        t_box.click()
        time.sleep(10)
        t_box.send_keys(message)                                   # Writing the message on Text Box
        send_button = chrome.find_element(By.XPATH,Send.send_button)
        time.sleep(10)
        send_button.click()
        time.sleep(25)
    def check_status(chrome):
        attrib = chrome.find_element(By.XPATH,'//*[@id="main"]/div[3]/div/div[2]/div[3]/div[56]/div/div/div/div[2]/div/div/span').get_attribute('aria-label')  # Checking the seen and sent status of the message
        print(attrib)
        i = 'Sent'
        q = 'Seen'
        if attrib==" Delivered ":  # Checking the sent and seen status to update the xlsx sheet
            i = i
            q = 'Not seen'
        return i , q

    def excel(i,q):
        workbook = xlsxwriter.Workbook('output.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', i)                            # Updating the xlsx Sheet
        worksheet.write('B1', q)
        workbook.close()
        print(i,q)