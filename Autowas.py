from selenium import webdriver
import sys,time
import xlrd                                                               #Importing necessary libraries for the code to work
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import xlsxwriter

s = Service("C:\\Users\\sheik\\Desktop\\Assignment 1 office\\chromedriver_win32\\chromedriver.exe")
options = webdriver.ChromeOptions()
message='Hello there!'

path='C:\\Users\\sheik\\Desktop\\Assignment 1 office\\number.xlsx'          #Importing the number from the excel sheet
ex=xlrd.open_workbook(path)
ed=ex.sheet_by_index(0)
p=(int(ed.cell_value(0,0)))
p=str(p)
number='0'+p
d="Delivered"

chrome = webdriver.Chrome(service=s)
chrome.get('https://web.whatsapp.com/')           #Going toh the whatsapp web server
time.sleep(35)

def Send_Text(number,message):      #Created a method for the whole process for sending message so it can be used in future to send more than one contact
    global attrib
    s_box = chrome.find_element(By.XPATH , '//*[@id="side"]/div[1]/div/label/div/div[2]')  #Finding search box to search number
    s_box.click()
    time.sleep(5)
    s_box.send_keys(number)                                  #Inputing the number from the xlsx file
    time.sleep(6)
    userclick=chrome.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span')
    userclick.click()
    time.sleep(10)
    t_box=chrome.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]') #Text box Operation
    t_box.click()
    time.sleep(5)
    t_box.send_keys(message)    #Writing the message on Text Box
    send_button=chrome.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/div/div[2]/div[2]/button/span')
    time.sleep(5)
    send_button.click()
    time.sleep(30)
    attrib =chrome.find_element(By.XPATH,'//*[@id="main"]/div[3]/div/div[2]/div[3]/div[20]/div/div/div/div[2]/div/div/span').get_attribute('aria-label') # Checking the seen and sent status of the message
    menu=chrome.find_element(By.XPATH,'//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
    menu.click()    #Finding the Three dot menu and clicking it.
    time.sleep(10)
    logout=chrome.find_element(By.XPATH,'//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]/div[1]') #Logout process
    logout.click()
try:
    Send_Text(number,message)
except NoSuchElementException as se:
    print('Oops!!time elaspsed try again by re-runnning the code') #If the user forgets to login the exception is handeled here.
    sys.exit()
i='Sent'
q='Seen'
if attrib==d:         #Checking the sent and seen status to update the xlsx sheet
    i=i
    q='Not seen'
workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1',i)              #Updating the xlsx Sheet
worksheet.write('B1', q)
workbook.close()

print(i,q)