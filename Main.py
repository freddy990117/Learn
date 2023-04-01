from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 設定開啟網頁

PATH = ("C:/Users/User/Desktop/Chromedriver.exe")
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com.tw/")
# 等待網頁開啟

WaitForPageOpen = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "q"))
)
# 點選輸入

Google_Search = driver.find_element(By.NAME, "q")
time.sleep(1)
Google_Search.click()
# 尋找輸入位置並輸入按下Enter

Search1 = driver.find_element(By.NAME, "q")
time.sleep(1)
Search1.send_keys("shopee")
Search1.send_keys(Keys.RETURN)
# 等待搜尋蝦皮頁面開啟

WaitForPageOpen2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "center_col"))
)

# 點選進入蝦皮頁面

Click2 = driver.find_element(
    By.CLASS_NAME, "VuuXrf")
Click2.click()

# 等待蝦皮頁面開啟

WaitForPageOpen3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "main"))
)

# 3/13 把 等待廣告開啟 刪除，因為已經有一個等待蝦皮頁面開啟，再寫一個多餘了
# 關閉廣告
# 自己寫的  差別在於 自己使用的是 尋找關閉視窗 + 點擊
# close_ad_button = driver.find_element(
#     By.CLASS_NAME, "home-popup__close-button")
# close_ad_button.click()

# 使用的是 尋找+模擬滑鼠 點擊其他的位置來關閉

action = ActionChains(driver)
# action.pause(5).perform()
action.click(driver.find_element(
    By.XPATH, '/html/body/div[1]/div/header/div[2]/div/a')).perform()

# 至蝦皮內搜尋
Shopee_Click_Search = driver.find_element(
    By.CLASS_NAME, "shopee-searchbar-input__input")
Shopee_Click_Search.click()

time.sleep(1)
# 3/14 要搜尋 Apple Watch 保護殼 再印出標籤網址
# 搜尋 Apple Watch
# ForUserSearch = input("請輸入你想搜尋的物品: ")
Shopee_Click_Search.send_keys("JV3C")
Shopee_Click_Search.send_keys(Keys.RETURN)

# 等待搜尋頁面開啟
WaitFor_SearchAppleWatch_PageOpen = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "sdzgsX")))

# 畫面開啟太快 等待2秒
time.sleep(2)

# 操控 滑鼠 點擊 JV3C台灣賣家

action2 = action.click(driver.find_element(
    By.CLASS_NAME, "shopee-search-user-item__leading"))
action2.perform()


# 因為只有點關鍵字 不會讓網頁刷新 所以用Sleep就好
# WaitFor_JV3C_PageOpen = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(
#         (By.CLASS_NAME, "shop-search-page__breadcrumb-link")))
time.sleep(10)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)
# 用 滑鼠 點擊 保護貼/保護殼
action3 = action.click(driver.find_element(
    By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div[10]'))
action3.perform()

# 畫面開啟太快 等待2秒
time.sleep(2)

# 點擊最熱銷
action = ActionChains(driver)
action.click(driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[3]')
             ).perform()

# 因為只有點關鍵字 不會讓網頁刷新 所以用Sleep就好
# WaitForPageOpen4 = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]')))
time.sleep(2)

# 將頁面往下滑 並點選第二頁

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

ClickToShopeePage2 = driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[3]/button[3]')
ClickToShopeePage2.click()

time.sleep(4)

# 點擊進入畫面
#
Clcik_IN_Search = driver.find_element(
    By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[2]/div/div[2]/div/div[6]')
Clcik_IN_Search.click()

# 等待 頁面 開啟

WaitForPageOpen_ForClick_In = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div/div[5]/div/div/button[1]')))

# 畫面開啟太快 要停頓一下才可以加入購物車 不知道為什麼
time.sleep(4)

# 點選加入購物車
Click_to_Shop_Car = driver.find_element(
    By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div/div[5]/div/div/button[1]')
Click_to_Shop_Car.click()

# 等待 畫面 開啟
Wait_For_Logi_Page = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "loginKey")))

# 尋找照號密碼並輸入

UserName = driver.find_element(By.NAME, "loginKey")
PassWord = driver.find_element(By.NAME, "password")
UserName.clear()
PassWord.clear()

UserName.send_keys("leejaytest")
PassWord.send_keys("Leejay0117")

UserName.send_keys(Keys.RETURN)

time.sleep(4)
WaitForBuyPageOpen = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[5]/div/div/button[2]')))
# 點選 商品 後 點選 直接購買

Produce = action.click(driver.find_element(By.XPATH,
                                           '//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div/div[4]/div/div[4]/div/div[1]/div/button[3]')
                       )
Produce.perform()

Produce2 = action.click(driver.find_element(
    By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[4]/div/div[4]/div/div[2]/div/button[2]')
)
Produce.perform()

time.sleep(5)
Buy_it = driver.find_element(
    By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div[5]/div/div/button[2]')
Buy_it.click()


# 因為要找很多的標籤，記的要加 S

# links = driver.find_elements(
#     By.CSS_SELECTOR, 'a[data-sqe="link"]')

# for link in links:
#     print(link.get_attribute("href"))

print("程式矇待奈")
time.sleep(5)
driver.quit()

# 3/10 可以點入 Youtube 發現是要點入的話 要看到Class Name 後面有 .com 後
# 換成 蝦皮 要按 XX
# 3/11 目前正求解，以為可以用點旁邊的方式跳過，但發現沒辦法
# 3/13 匯入 滑鼠.

# 3/17 成功印出連結，一直用 <div class :"col-xs-2-4 shopee-search-item-result__item 是不對的")
# 1.因為 上方只是一個存放標籤的位置，並不是指定的路徑，而我們可以更往裡面看到會有
# 2.一個 a 標籤裡面存放 href 的連結，「那我們就可以透過 a 標籤印出 href 的連結」
#
# 為何是使用 CSS_SELECTOR 'a[data-sqe="link"]' 來尋找 href 標籤
# 而不是使用 CSS_SELECTOR col-xs-2-4 shopee-search-item-result__item
# 使用 CSS_SELECTOR 'a[data-sqe="link"]' 來尋找 href 標籤是因為在 Shopee 的網頁架構中，
# 每個商品的連結都是包在 < a > 標籤中，且該 < a > 標籤具有屬性 data-sqe="link"。
# 因此，可以透過這個屬性來定位到商品連結的 < a > 標籤。

# 相較之下，使用 CSS_SELECTOR col-xs-2-4 shopee-search-item-result__item 是定位到商品的 < div > 標籤，
# 並不包含商品連結的資訊。如果要透過這個方式來取得商品連結，
# 還需要再進一步地查找該 < div > 標籤中包含連結資訊的元素，才能夠取得商品的連結。
# 因此，使用 CSS_SELECTOR 'a[data-sqe="link"]' 更為直接且有效率。

# 3/18 把商品加入購物車
