
"""
purpose of the program
"""

import math
import time
from selenium import webdriver

#Creating an object
driver= webdriver.Chrome()
driver.maximize_window()

#Fetching the url
driver.get("https://qainterview.pythonanywhere.com/")
#Checking title of the page
if(driver.title=="Factoriall"):
    print("The title is correct and we have accessed the correct page")
else:
    print("failedThe title does not match. Wrong page has loaded")
input_value = "asd"
text=driver.find_element_by_xpath("//input[@id='number']")

text.send_keys(input_value)
driver.find_element_by_xpath("//button[@id='getFactorial']").click()
time.sleep(4)
result=driver.find_element_by_xpath("//p[@id='resultDiv']").text
print(result)
if(type(result=='int')):
    res=int(result.split( )[-1])
print(res)
if(res==math.factorial(input_value)):
    print("The obtained result match the exepected result.Therefore the test is successfull")
else:
    print("The obtained result does not match the expected result.Therefore the test is failed")

driver.close()