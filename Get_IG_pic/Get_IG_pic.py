from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time
import os
import wget  # download用

Path = "E:/OneDrive - 國立成功大學/電機新手村/N-亂搞/1-網頁爬蟲/edgedriver/msedgedriver.exe"
driver = webdriver.Edge(Path)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username")))

passward = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))

username.clear()
passward.clear()
username.send_keys('yc.zonghan20')
passward.send_keys('janice55')

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login.click()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH,
         '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))

search.clear()
keyword = "#cats"

search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

# 等待跳轉
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'FFVAD')))

# 滑滾輪
for i in range(5):
    driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight);")  # 執行javaScript程式碼
    time.sleep(5)

imgs = driver.find_elements_by_class_name('FFVAD')

# 創建資料夾
path = os.path.join(keyword)
os.makedirs(path)

count = 1
for img in imgs:
    # print(img.get_attribure("src"))  # 取得src屬性
    save_as = os.path.join(path, keyword + str(count) + ".jpg")
    count += 1
    wget.download(img.get_attribute("src"), save_as)

print()
print("end")
time.sleep(30000)