from selenium import webdriver
from selenium.webdriver.common.by import By


#Keep the chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/?th=1')

price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
print(f'The price is {price_dollar.text}.{price_cents.text}$')
link = driver.find_element(By.XPATH, value='//*[@id="navFooter"]/div[4]/div/ul[4]/li[11]/a/h5')
print(link.text)

driver.get('https://www.python.org')
search_bar = driver.find_element(By.NAME, value='q')
print(search_bar.tag_name)
print(search_bar.get_attribute('placeholder'))
button = driver.find_element(By.ID, value='submit')
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
print(documentation_link.text)

#Close the single tab opened by Python
#driver.close()

#Closes each and every tab
driver.quit()