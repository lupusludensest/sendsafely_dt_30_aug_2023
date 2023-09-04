from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.plupload.com/examples/")
driver.find_element(By.ID, "uploader_browse").click()
time.sleep(2)

keyboard = Controller()

keyboard.type("C:\\Users\\rapid\\test_send_bug_report.jpg")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

driver.find_element(By.XPATH, "//span[normalize-space()='Start Upload']").click()

time.sleep(4)
driver.quit()