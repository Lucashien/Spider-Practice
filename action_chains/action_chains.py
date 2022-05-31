from selenium import webdriver
import selenium
from selenium.webdriver.common.action_chains import ActionChains

Path = "E:/OneDrive - 國立成功大學/電機新手村/N-亂搞/1-網頁爬蟲/edgedriver/msedgedriver.exe"
driver = webdriver.Edge(Path)
driver.get("https://tsj.tw")

action = ActionChains(driver)

# 取的各種標籤
blow = driver.find_element_by_id("click")
blow_count = driver.find_element_by_xpath(
    '//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')  # 因為h4標籤沒有特別的特徵，所以用xpath
items = []  # 有3個按鈕，所以用list
items.append(
    driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]'
    ))
items.append(
    driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]'
    ))
items.append(
    driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]'
    ))
prices = []
prices.append(
    driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(
    driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(
    driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))

action.click(blow)

for i in range(10000):
    action.perform()
    count = int(blow_count.text.replace("您目前擁有", "").replace("技術點", ""))
    print(blow_count.text.replace("您目前擁有", "").replace("技術點", ""))  # 提取純數字的部分
    for j in range(3):
        price = int(prices[j].text.replace("技術點", ""))
        if price <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(items[j])  # 移動到item購買的標籤
            upgrade_actions.click()
            upgrade_actions.perform()
            break

action.perform()  # 寫這個才會執行action_chains裡的動作
