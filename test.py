from selenium import webdriver
import GlobalFiles as gi
import os

driver = webdriver.Chrome()
driver.get('https://rpachallenge.com/')

downloadsFolder = os.path.expanduser("~/Downloads")

actionToStartDownload = driver.find_element('xpath', '//a[contains(text(), "Download Excel")]')

resultDownload = gi.waitForDownload(actionToStartDownload, 10)
print(resultDownload)