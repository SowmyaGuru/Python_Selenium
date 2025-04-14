from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

from Hpsmart import Last_Name

# to launch
driver = webdriver.Chrome()
# Initialize the WebDriver (example with Chrome)


# Set an implicit wait (optional)
driver.implicitly_wait(10)  # Implicit wait of 10 seconds

# Define the explicit wait
wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds

driver.get("https://automationexercise.com/")
driver.maximize_window()
time.sleep(10)

#Home_Button = driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[1]/a')

#Signup_Button = driver.find_elements('(//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
Signup_Button = driver.find_element(By.XPATH,'//div[contains(@class, "shop-menu")]/ul/li[4]')
Signup_Button.click()

Signup_Name_Field = driver.find_element(By.XPATH,'//input[@placeholder="Name"]')
Signup_Name_Field.send_keys("sowmya")


Signup_Name_Field = driver.find_element(By.XPATH,'//input[@data-qa="signup-email"]')
Signup_Name_Field.send_keys("sowmyaguru62@gmail.com")


Signup_Submit_Button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="signup-button"]')))
Signup_Submit_Button.click()

Gender_Radio = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="uniform-id_gender2"]')))
Gender_Radio.click()

Password_Field = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="password"]')))
Password_Field.send_keys("Rdl@12345")

#DOB days dropdown
DOB_Day_Drop = wait.until(EC.element_to_be_clickable((By.ID,"days")))
DOB_Day_Drop.click()
DOB_Day = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="days"]/option[5]')))
DOB_Day.click()

#DOB month dropdown
DOB_month_Drop = wait.until(EC.element_to_be_clickable((By.ID,"months")))
DOB_month_Drop.click()
DOB_month = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="months"]/option[5]')))
DOB_month.click()

#year drop down
DOB_year_Drop = wait.until(EC.element_to_be_clickable((By.ID,"years")))
DOB_year_Drop.click()
DOB_year = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="years"]/option[5]')))
DOB_year.click()

#checkbox
Checkbox1 = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="newsletter"]')))
Checkbox1.click()
Checkbox1 = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@id="optin"]')))
Checkbox1.click()

#First name
First_Name = wait.until(EC.element_to_be_clickable((By.ID,"first_name")))
First_Name.click()
First_Name.send_keys("Sowmya")

#First name
last_Name = wait.until(EC.element_to_be_clickable((By.ID,"last_name")))
last_Name.click()
last_Name.send_keys("Guruswamy")

#Address
Address = wait.until(EC.element_to_be_clickable((By.ID,"address1")))
Address.click()
Address.send_keys("Bangalore")


#Country

country = wait.until(EC.element_to_be_clickable((By.XPATH,'//select[contains(@id, "country")]')))
country.click()
country_selection = wait.until(EC.element_to_be_clickable((By.XPATH,'//select[contains(@id, "country")]/option[text()="India"]')))
country_selection.click()

#state
state = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[contains(@id, "state")]')))
state.send_keys("Karnataka")
city = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[contains(@id, "city")]')))
city.send_keys("Bangalore")
zipcode = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[contains(@id, "zipcode")]')))
zipcode.send_keys("Bangalore")
mobile_number = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[contains(@id, "mobile_number")]')))
mobile_number.send_keys("Bangalore")

#Create account button
Create_Account_Button = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Create Account"]')))
Create_Account_Button.click()






input("Do Code worked fine?")

