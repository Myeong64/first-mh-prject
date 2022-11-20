from selenium import webdriver
from selenium.webdriver.common.alert import Alert
# da = Alert(driver)
# da.accept()

from selenium import webdriver

# USB 장치 에러 메세지 없애기
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox()
# driver.get("http://localhost:8000")

# # [...]

# alert = driver.switch_to_alert() # driver.switch_to_alert()을 호출하면 alert에 대한 객체를 넘겨준다.

# assert "alert창" in alert.text  # alert text 얻기

# alert.accept()  # alert 확인

# alert.dismiss() # alert 취소

import os
import keyboard




from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# driver = webdriver.Chrome (executable_path="C:\\chromedriver.exe")
# maximize with maximize_window()
# driver.maximize_window()
# driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
# # identify element and click()
# l=driver.find_element_by_name("submit")
# l.click()
# // alert_is_present() expected condition wait for 5 seconds

# try:
#    WebDriverWait(driver, 5).until (EC.alert_is_present())
#    // switch_to.alert for switching to alert and accept
#    alert = driver.switch_to.alert
#    alert.accept()
#    print("alert Exists in page")
# except TimeoutException:
#    print("alert does not Exist in page")
# driver.close()

# 다른회원님이 예약중입니다. 다른시간대를 선택해주세요.--- 확인 누르면 티시간화면으로 이동.
# 이미 다른 회원님이 예약을 하였습니다.  죄송합니다! ---> 달력화면으로 자동 이동.
# Message: unexpected alert open: {Alert text : 이미 다른 회원님이 예약을 하였습니다.  죄송합니다!}

str1 = "다른"
if str1 in "다른 고객 문자열입니다":
    print(True)
# Output True
 
if "른" not in str1:
    print(False)
# Output False

# from PIL import ImageGrab
# import pyautogui as pag

# screen = ImageGrab.grab()

# poss = pag.position()
# print(poss)

# screen.getpixel(pos)


atext = "17일"
btext = "12일"

ctext = "2022년 1월 12일 월요일"

if btext in ctext :
    print(atext, ctext)
else :
    print("none !!")


tee_list = []

temp = range(11,15)
length_t = len(temp)
print(length_t)
for i in range(0, length_t):
    tee_list.append(temp[i])

temp = range(15,25)
length_t = len(temp)
print(length_t)
for i in range(0, length_t):
    tee_list.append(temp[i])

temp = range(11,5,-1)
length_t = len(temp)
print(length_t)
for i in range(0, length_t):
    tee_list.append(temp[i])

print(tee_list)


teelist1 = [1,2,3,4,5]
teelist2 = [7,8,9]

teelist2.reverse()

tee12 = teelist1 + teelist2

print(tee12)

temp_list = []
for i in range(0,10):
    temp_txt = str(i) + "temp \n"
    temp_list.append(temp_txt)
    
print(temp_list)


family = ['mother', 'father', 'gentleman', 'sexy lady']

for x in family:        # family의 각 항목 x에 대하여:
    print(x, len(x))    # x와 x의 길이를 출력하라.
    gy_tm_text = x
    
    if "a" in gy_tm_text :
        print(gy_tm_text)
        
    print("-0 ", gy_tm_text[-0])
    print("-1 ", gy_tm_text[-1])
    print("-2 ", gy_tm_text[-2])
    print("-3 ", gy_tm_text[-3])
    print("-4 ", gy_tm_text[-4])
    