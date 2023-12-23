from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

def upgrade():
     store = [s for  s in driver.find_elements(By.CSS_SELECTOR, value="#store div") if s.text != "" and "grayed" not in s.get_attribute("class") and "amount" not in s.get_attribute("class")]
     to_buy = None
     for item in store:
          money = int(driver.find_element(By.ID, value="money").text.replace(",",""))
          if money > int(item.text.split("-")[1].strip().split("\n")[0].replace(",","")):
               to_buy = item
     if to_buy is not None and int(to_buy.text.split("-")[1].strip().split("\n")[0].replace(",","")) >= int(store[0].text.split("-")[1].strip().split("\n")[0].replace(",","")):         
          to_buy.click()

global launch 
launch = True

def stop():
     global launch
     launch = False
     cookieperseconds = driver.find_element(By.ID, value="cps")
     print(cookieperseconds.text)

schedule.every(1).seconds.do(upgrade)
schedule.every(5).minutes.do(stop)
          
while launch:
     cookie.click()
     schedule.run_pending()





 
