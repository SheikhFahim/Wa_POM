
# Whatsapp UI Automation Using Python And Selenium

This project is a total automation of  Whatsapp User where the user logs in to the app and search for a contact. Furthermore , the user sends a text message to the contact message and checks whether the
message is sent or seen by the contact.Lastly, the user logs out of the system automatically.This whole
project is built with Python and Selenium.


## Author

- [@Sheikh Fahim Uzzaman](https://github.com/SheikhFahim)


## Requirements

**Os:** Windows/Mac/Linux

**Language:** Python

**IDE:** Pycharm (Or any IDE that supports Python 3 or above)



## Workflow
1)Firstly, i have imported various libraries that are shown in the first para of my code

2)For the first test case we neede to scan the QR code and get into the whatsapp web version so 
we used the selenium chrome web driver for that with some delay cause it takes some time to get 
the web pages to load.

3)Then we used the xlrd library to take input of number from the xlsx file as per our given 
requirements.

4)After that we declared a function where we will be doing our whole automation project. The 
main reason for the function calling was done so that we can use that exact same code for the 
multiple user in the future.So, there will be room for other coders to make it more feasible.

5)In the function first we used XPATH method that is available in the selenium we copied the 
XPATH code from the HTMl verison of the web and we created the paths by calling the find_elements()
function.

6)Here is a experience i want to share if you get the error for deprecation just create an object from the service class as i have done in my code.
Also, use the find_elements method instead of find_elements_by* cause it is deprecated.

 7)The whole workflow is done by stepwise and clicking on the XPATH of the whatsapp web version.Also, the delays are added so that the web page gets enough time to get refreshed.





## Features

- Takes a Valid number using the Excel File
- Searches for that contact
- Automatically generates messgae and sends it.
- Let the user know whether the message is sent or seen/not seen.

