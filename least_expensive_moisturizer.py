import time
import itertools
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(3)
driver.maximize_window()
time.sleep(6)

#check if the heading of the page matches so that we can confirm we have landed on the right page
if(driver.find_element_by_xpath("//h2").text=="Moisturizers"):
    print("Successfully entered the Moisturizer shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)
#find all the elements on the page which contains 'Aloe' in it
aloe=driver.find_elements_by_xpath("//p[contains(text(),'Aloe')]/following-sibling::p")
almond=driver.find_elements_by_xpath("//p[contains(text(),'Almond')]/following-sibling::p")
moisture=[almond,aloe]

#assign an initial minimum price and iterate comparing the prices of all the elements to the minimum price and assign the new minimum price
min_value=10000
for condition in moisture:
    for each_element in condition:
        #split and extract the prices of item in integer format    
        price_moisturizer=int(each_element.text.split()[-1])
        
        if(price_moisturizer<min_value):
            min_value=price_moisturizer
    #find and click the Add button corresponding to the minimum price
    driver.find_element_by_xpath("//p[contains(text(),'%d')]/following-sibling::button"%min_value).click()
    time.sleep(1)      
    print("the moisturizer added to the cart is %s and its price is %d"%(driver.find_element_by_xpath("//p[contains(text(),'%d')]/preceding-sibling::p"%min_value).text,min_value))    
    time.sleep(1)
