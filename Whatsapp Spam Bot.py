from selenium import webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')
driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
inputString = input("Enter message to send: ")
for i in range(int(input("Enter number of times to spam: "))):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
