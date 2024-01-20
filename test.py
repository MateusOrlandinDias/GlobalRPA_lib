import GlobalUi as gui
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://test.pypi.org')

test = gui.element_exists(driver, "//label[contains(text(), 'Username')]", 5)
print(test)