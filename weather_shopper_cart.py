"""
Program to check the shopping cart and fill payment details

"""
import time
from selenium import webdriver

#create object for webdriver
driver=webdriver.Chrome()
driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
time.sleep(3)
#check if have landed on the correct page
if(driver.find_element_by_xpath("//h2").text=="Moisturizers"):
    print("Successfully entered the sunscreen shopping site")
else:
    print("Failed to to enter the desired page.")
time.sleep(2)

#find the location of the cart
cart_before=driver.find_element_by_xpath("//button[@onclick='goToCart()']").text

#extract the quantity of items in the cart
cart_before_split=cart_before.split()[-1]
print(cart_before_split)
sum=0
items=[]
#Find and click the buttons to add the items into the cart
for i in range(1,7):
    driver.find_element_by_xpath("(//button[contains(@class,'btn btn-primary')][text()='Add'])[%d]"%i).click()
    #Find the total sum of elements incrementally as they are added
    sum=sum+int(driver.find_element_by_xpath("(//button[@class='btn btn-primary'][text()='Add'])[%d]/preceding-sibling::p[contains(text(),'Price')]"%i).text.split()[-1])
    #Store the elements as they are added into the list
    items.append(driver.find_element_by_xpath("(//button[@class='btn btn-primary'][text()='Add'])[%d]/preceding-sibling::p[@class='font-weight-bold top-space-10']"%i).text)
print(sum)
print(items)
time.sleep(2)
#find the location of the cart after adding items
cart_after=driver.find_element_by_xpath("//button[@onclick='goToCart()']").text
print(cart_after)
#extract the quantity of items in the cart
cart_after_split=cart_after.split()[2]
print(cart_after_split)

#check if the cart before matches with cart after adding item
if(cart_after_split==cart_before_split):
    print("Failed to add items into the cart")

final_items=int(cart_after_split)

#check if all items are correctly added to the cart
if(final_items<6):
    print("Some of items not added to the cart")

#check if extra items are added to the cart
if(final_items>6):
    print("Additional items added to the cart")

#check if all the items added are successfully reflects in the cart
if(final_items==6):
    print("Successfully added items into the cart")

#Find and click on the cart button
driver.find_element_by_xpath("//span[@id='cart']").click()
time.sleep(6)
if(driver.find_element_by_xpath("//h2").text=="Checkout"):
    print("Successfully arrived at the checkout page")
else:
    print("Failed to arrive at the checkout page")

#find the final total displayed on the screen
price=int(driver.find_element_by_xpath("//p[@id='total']").text.split()[-1])
print(price)

#compare if the final total matches with the sum calculated
if(price==sum):
    print("The total is correct")
else:
    print("wrong total")
list_one=[]
#store the list of items displayed in checkout page into a list
for i in range(final_items):
    list_one.append(driver.find_element_by_xpath("(//td)[%d]"%(2*i+1)).text)
print(list_one)
#check if the final list of items matches with the selected items
if(list_one.sort()==items.sort()):
    print("All the items selected are properly displayed")
else:
    print("the items selected does not match with the final list of items")

#locate and click the pay button
driver.find_element_by_xpath("//span[text()='Pay with Card']").click()
time.sleep(2)

#switch to frame
iframe=driver.find_element_by_xpath("//iframe[@name='stripe_checkout_app']")
driver.switch_to_frame(iframe)

#Locate and fill in the payment details
driver.find_element_by_xpath("//input[@type='email']").send_keys("akkul.dn@qxf2.com")
driver.find_element_by_xpath("//input[@placeholder='Card number']").send_keys("4242 4242 4242 4242")
driver.find_element_by_xpath("//input[@placeholder='MM / YY']").send_keys("0135")
driver.find_element_by_xpath("//input[@placeholder='CVC']").send_keys("498")
driver.find_element_by_xpath("//input[@placeholder='ZIP Code']").send_keys("560016")

#Locate and click the submit button
driver.find_element_by_xpath("//button[@type='submit']").click()