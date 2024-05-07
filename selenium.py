from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("C:/Users/WINDOWS 11/Desktop/Web_Scriping/pdf2html/output.html") 
time.sleep(2) 

name_field = driver.find_element_by_id("fillname") 
name_field.clear() 
name_field.send_keys("Krinjal Mali") 

father_name_field = driver.find_element_by_id("father_name") 
father_name_field.clear()
father_name_field.send_keys("Tejmal Mali") 

father_employment_field = driver.find_element_by_id("father_employment")  
father_employment_field.clear()
father_employment_field.send_keys("Bussinessman")  

identification_marks_field = driver.find_element_by_id("identification_marks")  
identification_marks_field.clear()
identification_marks_field.send_keys("Nothing") 

submit_button = driver.find_element_by_id("submit")  
submit_button.click()

