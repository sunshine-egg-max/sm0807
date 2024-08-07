from selenium import webdriver # 匯入(import)操控瀏覽器相關的程式
from selenium.webdriver.common.keys import Keys # 操作瀏覽器互動的程式
from selenium.webdriver.common.by import By # DOM TREE 搜尋節點的類別集
import time

driver = webdriver.Firefox() # 生成一個由程式操控的 Firebox
driver.get("http://www.python.org") # 訪問 python.org
assert "Python" in driver.title # 檢查分頁名稱是否包含 Python
time.sleep(5)

# https://selenium-python.readthedocs.io/locating-elements.html
elem = driver.find_element(By.NAME, "q") # 等同於 BeautifulSoup 的 find
# elem = driver.find_element(By.CLASS_NAME, "search-field")
# elem = driver.find_element(By.ID, "id-search-field")
time.sleep(5)

elem.clear() # 清除搜尋欄
elem.send_keys("pycon") # 輸入 pycon 到搜尋欄
time.sleep(5)

elem.send_keys(Keys.RETURN) # 按下鍵盤的 ENTER
time.sleep(5)

assert "No results found." not in driver.page_source # "No results found" 未出現在頁面上
driver.close() # 關掉當前分頁
driver.quit() #關掉整個模擬瀏覽器

print("Done") 