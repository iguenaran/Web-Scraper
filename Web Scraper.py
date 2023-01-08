import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# webdriver
s = Service("C:\\Users\\maria\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.worlddata.info/highest-mountains.php')
# html
content = driver.page_source
html_page = driver.page_source
soup = BeautifulSoup(driver.page_source, 'html.parser')

bold_style_1 = soup.find_all('td', attrs={'style': 'font-weight: bold; font-size:12px; text-align:left'})
bold_style_2 = soup.find_all('td', attrs={'style': 'font-weight: bold;'})

list1 = []
list2 = []

for item in bold_style_1:
    list1.append(item.text)

for item in bold_style_2:
    list2.append(item.text)

# csv file
df = pd.DataFrame({'Country':list2, 'mountains':list1})

df.to_csv('mountains.csv')


driver.close() 
