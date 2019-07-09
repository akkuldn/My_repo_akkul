"""
 Program to add most expensive item from moisturizer page into the cart
"""
import time
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(3)
#check if have landed on the correct pages and click
if(driver.find_element_by_xpath("//H2").text=="Moisturizers"):#change
    print("Successfully entered the sunscreen shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)
prices=driver.find_elements_by_xpath("//P")
print(prices)
