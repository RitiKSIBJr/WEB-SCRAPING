from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import csv

driver_option = webdriver.ChromeOptions()
driver_option.add_argument('headless')
driver_option.add_argument('windows-size=1200x600W')
chromedriver_path = r"C:\Users\lette\Downloads\chromedriver_win32\chromedriver.exe"

def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path,chrome_options=driver_option)

browser = create_webdriver()
browser.get("https://stackoverflow.com/questions?pagesize=50&sort=newest")

projects = browser.find_elements(By.XPATH, "//h3[@class='s-post-summary--content-title']")

i=0
data = []

for project in projects:
    title = project.text
    url = project.find_elements(By.XPATH,'//a[@class="s-link"]')
    url = url[i].get_attribute('href')
    problem_list = {'Problem':title, 'URL':url}
    data.append(problem_list)
    i = i + 1


browser.quit()

with open('stack.csv', 'a') as file:

    writer = csv.DictWriter(file, fieldnames=['Problem', 'URL'])
    for line in data:
        writer.writerow(line)
