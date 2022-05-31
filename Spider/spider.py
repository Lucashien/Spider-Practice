from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = "E:/OneDrive - 國立成功大學/電機新手村/N-亂搞/1-網頁爬蟲/edgedriver/msedgedriver.exe"

driver = webdriver.Edge(Path)
driver.get("https://www.dcard.tw/f")
search = driver.find_element_by_name("query")  # 尋找html的input標籤,name = query
search.clear() # 清空搜尋欄
search.send_keys("比特幣")  # 輸入文字
search.send_keys(Keys.RETURN)  # 按enter

# 等待搜尋結束後出現標籤再進行下一步    p.s.跳轉頁面書要時間
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sc-3yr054-0")) 
    )


titles = driver.find_elements_by_class_name("tgn9uw-3")  # titles 為 list

for title in titles:
    print(title.text)


driver.back()

time.sleep(5)
driver.quit()