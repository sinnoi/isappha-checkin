from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
username = (input('Student ID : '))
password = (input('Password : '))

url = 'http://isappha.com/istudent/index.php?r=site/studentLogin&persontype=3'
url_clock = 'http://isappha.com/istudent/index.php?r=sys_student/detail/timeStempOnline'
driver = webdriver.Edge('C:\\Users\\66651\\Desktop\\edgedriver_win64\\msedgedriver.exe')
driver.get(url)
driver.maximize_window()
driver.find_element(By.ID, 'student_code').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

sleep(1)

driver.get(url_clock)

driver.find_element(By.CLASS_NAME, 'btn.btn-primary.btn-large').click()

sleep(1)

driver.find_element(By.CSS_SELECTOR, '.modal-footer .btn+.btn').click()
