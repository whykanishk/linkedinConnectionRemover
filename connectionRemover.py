from selenium import webdriver
from time import sleep

mailID = input("Enter your LinkedIn E-Mail: ")
password = input("Enter your LinkedIn Password: ")
driverpath = input("Enter the PATH where Chrome driver is kept: ").replace("\\","/") + "/chromedriver.exe"
page = input("Enter page after where you want to remove invitations: ")

try:
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://www.linkedin.com/")
    driver.find_element_by_id("session_key").send_keys(mailID)
    driver.find_element_by_id("session_password").send_keys(password)
    driver.find_element_by_xpath("//html/body/main/section[1]/div[2]/form/button").click()
    driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/?filterCriteria=&invitationType=&page={}".format(page))
    while True:
        driver.find_element_by_xpath("//html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section/div[2]/ul/li[1]/div/div[2]/button").click()
        sleep(2)
        driver.find_element_by_xpath("//html/body/div[3]/div/div/div[3]/button[2]").click()
        sleep(2)
except:
    print("Session End")
