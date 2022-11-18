from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import csv

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("headless")
driver_option.add_argument("window-size=1200x600W")
chromedriver_path = r"C:\Users\lette\Downloads\chromedriver_win32\chromedriver.exe"

def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path,chrome_options=driver_option)


browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")
projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

dataset = []

for project in projects:
    project_name = project.text
    project_url = project.find_element(By.XPATH,'//*[1][name()="a"]').get_attribute('href')
    project_list = {'Name': project_name, 'URL': project_url}
    dataset.append(project_list)

browser.quit()

with open('data.csv', 'w') as file:

    writer = csv.DictWriter(file,fieldnames=['Name', 'URL'])
      
    
    for line in dataset:
        writer.writerow(line)




