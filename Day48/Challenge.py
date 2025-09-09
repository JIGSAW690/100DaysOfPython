from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep the chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')

event_dict = {}


dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# Build dictionary
for n in range(len(dates)):
    event_dict[n] = {
        'time': dates[n].text,
        'name': events[n].text,
    }


print(event_dict)

#driver.quit()