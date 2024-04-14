from selenium import webdriver
from selenium.webdriver.common.by import By

# code to keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B09V3JJT5D/ref=fs_a_ipt2_us2")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-offscreen")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar}.{price_cents}")
