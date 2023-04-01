from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import wget
# 建立開啟資訊

PATH = ("C:/Users/User/Desktop/chromedriver.exe")
driver = webdriver.Chrome(PATH)
Mouse = ActionChains(driver)
driver.get("https://www.instagram.com/")

# 等待IG畫面開啟 這邊用 Play 商店圖示
Wait_IGLoginPage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_aa5q"))
)

# 輸入帳戶與密碼並登入
UserName = driver.find_element(By.NAME, "username")
PassWord = driver.find_element(By.NAME, "password")
UserName.clear()
PassWord.clear()
UserName.send_keys("leejaytest")
PassWord.send_keys("leejay0117")
time.sleep(1)
UserName.send_keys(Keys.RETURN)

# # 進入IG等待畫面
time.sleep(5)

# 點選搜尋並搜尋
Click_Search = Mouse.click(driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]'))
Click_Search.perform()

keyword = "#cbum"
Search = driver.find_element(By.CLASS_NAME, "_aauy")
Search.send_keys(keyword)

time.sleep(1)

Click_SearchOptiton = Mouse.click(driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]'))
Click_SearchOptiton.perform()

time.sleep(8)
# 等待頁面開啟
# Wait_SearchPage = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "_aagv"))
# )

# 印出  src
# 這邊一開始用 x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3 來做定位 → NO  css aagv aagu → NO
# 最後用 class name 的 第一個元素來定位 就可以印出來了
Print_src = driver.find_elements(
    By.CLASS_NAME, "x5yr21d")

# --------------後面是照著做的

# 創建資料夾
path = os.path.join(keyword)
os.mkdir(path)

count = 0
for i in Print_src:
    save_as = os.path.join(path, keyword + str(count) + '.jpg')
    wget.download(i.get_attribute("src"), save_as)
    count += 1
    # print(i.get_attribute("src"))


time.sleep(5)
