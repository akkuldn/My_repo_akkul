"""
 Program to add most expensive item from moisturizer page into the cart
"""
import time
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(3)
#check if have landed on the correct page

#check if the heading of the page matches so that we can confirm we have landed on the right page
if(driver.find_element_by_xpath("//H2").text=="Moisturizers"):
    print("Successfully entered the sunscreen shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)

#find prices of all the elements
prices=driver.find_elements_by_xpath("//p[contains(text(),'Price')]")

#assign an initial maximum price and iterate comparing the prices of all the elements to the max price and assign the new maximum price
max_price=1
for i in range(6):
    #get the integer value of price
    prices_new=int(prices[i].text.split()[-1])
    if(prices_new>max_price):
        max_price=prices_new
   
print(max_price)
#find the button corresponding to the max price and click it
driver.find_element_by_xpath("(//P[contains(text(),'%d')])/following-sibling::BUTTON"%max_price).click()
