from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time, threading, autoit, random

#Settings Web Driver
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

#Open Browser
driver = webdriver.Chrome(chrome_options=option, executable_path=r"C:\Users\ASUS\Documents\Python Scripts\chromedriver.exe")

#Go To Profile
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/yunasan.hyuuga")

#Login
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit   = driver.find_element_by_id("loginbutton")
username.send_keys("YOUR EMAIL")
password.send_keys("YOUR PASSWORD")
submit.click()

def UploadFotoProfil():
    #Perbarui Foto
    driver.implicitly_wait(7)
    perbarui = driver.find_element_by_xpath("//*[@id='u_0_15']")
    perbarui.click()
    driver.implicitly_wait(7)
    unggahFoto = driver.find_element_by_class_name("_3cia")
    driver.implicitly_wait(5)
    unggahFoto.click()

    #Pilih FILE
    time.sleep(5)
    autoit.control_focus("Open", "Edit1")
    index = random.randint(1, 15)
    index = str(index)
    autoit.control_set_text("Open", "Edit1", "C:\\flutter\\pin\\"+index+".jpg")
    autoit.control_click("Open", "Button1")
    time.sleep(5)
    #autoit.send("{ENTER}")
    #Upload File

    time.sleep(5)
    driver.implicitly_wait(5)
    upfile = driver.find_elements_by_class_name("_4jy0 _4jy3 _4jy1 _51sy selected _42ft")
    upfile.submit()

    #LOOP per Hour
    threading.Timer(3600, UploadFotoProfil).start()
    #Random File
UploadFotoProfil()