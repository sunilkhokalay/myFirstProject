import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class gmail:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.driver.get("http://gmail.com")
        time.sleep(5)

    def login(self):
        usernameField = self.driver.find_element_by_id('Email')
        usernameField.send_keys(self.username)
        nextButton = self.driver.find_element_by_id('next')
        nextButton.click()
        time.sleep(2)
        passwordField = self.driver.find_element_by_id('Passwd')
        passwordField.send_keys(self.password)
        signInButton = self.driver.find_element_by_id('signIn')
        signInButton.click()
        try:
            doneButton = self.driver.find_element_by_link_text('Done')
            if doneButton:
                doneButton.click()
        except Exception as e:
            print ("No Security Check.. Msg-{}".format(e))
        time.sleep(2)

    def sendMail(self,to,subject,message):
        composeMailButton = self.driver.find_element(By.CSS_SELECTOR,"div[class='T-I J-J5-Ji T-I-KE L3']")
        composeMailButton.click()
        time.sleep(2)
        toField = self.driver.find_element_by_name('to')
        toField.send_keys(to)
        time.sleep(1)
        subjectField = self.driver.find_element_by_name('subjectbox')
        subjectField.send_keys(subject)
        time.sleep(1)
        messageField = self.driver.find_element(By.CSS_SELECTOR,"div[class='Am Al editable LW-avf']")
        messageField.send_keys(message)
        time.sleep(1)
        sendButton = self.driver.find_element(By.CSS_SELECTOR,"div[class='T-I J-J5-Ji aoO T-I-atl L3']")
        sendButton.click()
        time.sleep(10)

    def quit(self):
        self.driver.quit()

obj = gmail('sunilkhokalay','sunil@aricent')
time.sleep(10)
obj.login()
time.sleep(10)
obj.sendMail('skumarkh@cisco.com','Hiii',"Hi This is automated mail!!!")
time.sleep(10)