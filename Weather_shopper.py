"""
  Program to select Moisturizer or Sunscreen based on the temperature
"""
import time
from selenium import webdriver
#Create object for webdriver
driver=webdriver.Chrome()

#function to check and print wether we have successfully landed on the Sunscreen page or the moisturrizer page
def statement_print(heading_path,temperature):
    if(heading_path=='Sunscreens' and temperature>=34):
        print("successfully entered the Sunscreen page")
    elif(heading_path=='Moisturizers' and temperature<=19):
        print("successfully entered the Moisturizer page")
    else:
        print("Failed to access the site,please check")
        
if __name__=='__main__':
    #to go the the weather shopper site 
    url=driver.get("https://weathershopper.pythonanywhere.com/")
    time.sleep(2)
    
    #Check wether we have landed on the correct page    
    if(driver.title=='The best moisturizers in the world!'):
        print("Successfully Entered the weather shopper website")
    else:
        print("Please check the url")

    time.sleep(3)
    
    #find the temperature from the webpage
    temperature=driver.find_element_by_xpath("//span[@id='temperature']").text.encode("utf-8")

    #extract the temperature in integer format
    temperature=int(temperature.split()[0])    
    print(temperature)
    
    time.sleep(3)
    #check if temperature is below 19 degree celcius or above 34 degree and select moisturizer or sunscreen appropriately
    if(temperature<=19):
    #Find the button to buy moisturizer and click it
        driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()        
    #Find the button to buy Sunscreen and click it
    elif(temperature>=34):
        driver.find_element_by_xpath("//button[text()='Buy sunscreens']").click()
    #find the heading of the page we have landed on    
    heading_path=driver.find_element_by_xpath("//h2").text
    #call the function to print wether we have landed on the sunscreen page or the moisterizer page 
    statement_print(heading_path,temperature)

driver.close()