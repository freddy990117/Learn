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
driver.get("https://shopee.tw/")
Mouse = ActionChains(driver)

# 出現廣告，先點選其他地方將廣告關閉 (這邊選擇點選登入)
CloseAdd = Mouse.click(driver.find_element(By.XPATH,
                                           '//*[@id="main"]/div/header/div[1]/nav/ul/a[3]'))
CloseAdd.perform()

Login = Mouse.click(driver.find_element(By.XPATH,
                                        '//*[@id="main"]/div/header/div[1]/nav/ul/a[3]'))
Login.perform()

# 等待蝦皮登入畫面開啟
ShopeeLoginPage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, 'loginKey'))
)

# 輸入帳號與密碼
Account = driver.find_element(By.NAME, "loginKey")
PassWord = driver.find_element(By.NAME, 'password')
Account.clear()
PassWord.clear()
Account.send_keys("leejaytest")
PassWord.send_keys("Leejay0117")
time.sleep(1)
Account.send_keys(Keys.RETURN)

# 等待開啟頁面
time.sleep(3)

# 出現廣告，先點選其他地方將廣告關閉 (這邊選擇點選登入)

FindSearch = driver.find_element(
    By.CLASS_NAME, 'shopee-searchbar-input__input')
FindSearch.send_keys("情趣內衣")
FindSearch.send_keys(Keys.RETURN)

# 等待搜尋畫面開啟
WaitForSearchPageOpen = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]'))
)
MostPopular = driver.find_element(
    By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[1]/div[3]')
MostPopular.click()

time.sleep(4)

ChooseProduce = Mouse.click(driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[1]/a/div/div'))
ChooseProduce.perform()

time.sleep(3)

# 使用滑鼠選擇 顏色
ChooseColor = Mouse.click(driver.find_element(By.CSS_SELECTOR,
                                              'button[aria-label="黑色單件三角內褲"]')).perform()
# 使用滑鼠選擇 尺寸
ChooseSize = Mouse.click(driver.find_element(By.CSS_SELECTOR,
                                             'button[aria-label="L"]')).perform()

time.sleep(2)

# 按下購買鍵
Buyit = Mouse.click(driver.find_element(
    By.CSS_SELECTOR, "button[class= 'btn btn-solid-primary btn--l iFo-rx']")).perform()

time.sleep(5)
CheckOut = driver.find_element(
    By.CSS_SELECTOR, 'button[class="shopee-button-solid shopee-button-solid--primary"]')
CheckOut.click()

time.sleep(5)


# 3/25 因為下單後重新登入要在點選一次，所以把登入往前移動
# 發現新增資料時要選擇地址那邊沒有元素 還沒學到那邊 先給他放棄
