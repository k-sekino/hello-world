#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re #like_css, src関連
def waitload(id_of_element, clickflag): #1だとクリック、0だとクリックしない
    while(1):
        elements = driver.find_elements_by_id(id_of_element) #By.id
        if (len(elements) > 0):
            if (clickflag == 1):
                elements[0].click()

            break #breakしない可能性？

    return 1

def waitload_tag(tagname_of_element, clickflag): #1だとクリック、0だとクリックしない
    while(1):
        elements = driver.find_elements_by_tag_name(tagname_of_element) #By.id
        if (len(elements) > 0):
            #if (clickflag == 1):
                #elements[0].click()

            break #breakしない可能性？

    return 1


def getelement_by_outerHTML(tagname, string, clickflag):
    elements = driver.find_elements_by_tag_name(tagname)
    for element in elements:
        argument = element.get_attribute("outerHTML")
        if (string in argument):
            if (clickflag == 1):
                element.click()

            return 1 #forからぬける

    return 0

def getelements_like_css(selector_of_element, string, arr, clickflag): #1だとクリック、0だとクリックしない
    r_flag = 0
    #len_of_arr = len(arr)
    elements = driver.find_elements_by_css_selector(selector_of_element) #By.id
    for i, element in enumerate(elements):
        argument = element.get_attribute("outerHTML")
        if (string in argument):
            r_flag += 1
            if (clickflag == 1):
                element.click() #遷移してもelementsに前のページが保存されてる?
            
            #return (i+1) #forからぬける 禁煙o,喫煙-,05x,25xのとき3だった
            #先頭のxが読まれる


        #else:
        argument_src = element.get_attribute("src")
        #argument_short = argument_src[-17:-4]
        argument_short = re.findall('seat_[a-zA-Z]+', argument_src)
        if (len(argument_short) > 0): #この時点でseat_**的な文字列の存在は確定
            #maru, sankaku, fin, noみたいなのを取得
            argument_rev = argument_short[0]
            argument_rev = re.findall('_[a-zA-Z]+', argument_rev)[0]
            argument_rev = re.findall('[a-zA-Z]+', argument_rev)[0]

            if (len(arr) < i+1):
                arr.append(argument_rev) #string
            else:
                arr[i] = argument_rev

        else: #グリーンマークとか?
            if (len(arr) < i+1):
                arr.append('?')
            else:
                arr[i] = '?'
 

    print(arr)
    return r_flag


def javascript_click(id_of_element):
    string = "document.getElementById('" + id_of_element + "').click()"
    driver.execute_script(string)
    #driver.execute_script("document.getElementById('BtnVacantSeatInquiry').click()")
    return 1

def u_sleep(x):
    time.sleep(x/1000000.0)
    return

from selenium import webdriver # さっきpip install seleniumで入れたseleniumのwebdriverというやつを使う
import time
import random

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.by import By


#options = webdriver.ChromeOptions() #ChromeOptions()
#chromeとfirefoxで変更？↑↓ 5箇所??
#options.add_argument("user-data-dir=./sample_profile") #Path to your chrome profile
#driver = webdriver.Chrome(executable_path="/home/sekino/selenium_driver/chromedriver", chrome_options=options) #chrome_options
#chromedriver
#geckodriver

#/usr/local/bin に入れとけばいい

# $ firefox -P
# 一旦ダイアログから手動で、profileつかってアクセスしてログインしとく
# すると次回以降予測ででてきたり
fp = webdriver.FirefoxProfile("/home/sekino/.mozilla/firefox/drcfb47m.test_profile")

# 画像を読み込まない
fp.set_preference("permissions.default.image", 2)

driver = webdriver.Firefox(fp) #fp

#System.setProperty("webdriver.firefox.profile", "myprofile") #namae
#WebDriver driver = new FirefoxDriver();

time.sleep(1) #ときどきwindow_sizeとpositionが変わらないことがある

time.sleep(2)
driver.set_window_size(1020,650) #1300,800 996,577
driver.set_window_position(170,0)
current_size = driver.get_window_size()
print(current_size)

#start = time.time() #chrome起動して軽めのページに一度アクセス?
#driver.get("http://jr-mars.dyndns.org/m/index.php") #0.67s 
#driver.get("https://www.if.t.u-tokyo.ac.jp/~mita/EInfo/happyo/index.php?nendo=2009") #1.31s httpsはおそそう
#driver.get("http://www.eki-net.com/hoge") #0.31s
#driver.get('http://www.ekikara.jp/cgi-bin/find.cgi')
#duration = time.time() - start
#print("duration: " + str(duration))

print(driver.current_url)

#print("Which mode? 1: only once 2: repeated")
#test_str = input() #raw_input()
#print("mode == " + test_str)

cancel_css_str = (
#"window.addEventListener('load', function() {"

#"document.write(document.styleSheets.length);"
"for(var i = 0; i < document.styleSheets.length; i++) {"
#"var styleSheetPath = document.styleSheets[i].href;"
#"var filename = styleSheetPath.substring(styleSheetPath.lastIndexOf('/')+1, styleSheetPath.length);"
#"if (1) {"
"document.styleSheets[i].disabled = true;"
#"}"
"}"

#"});"
)

print(cancel_css_str)

old_url = "v4qnolweioo034u8qo"
cur_url = "awfevj034j89q2jrio"
#try, catch?
#wait_test = WebDriverWait(driver, 30) #sec
#wait_about_url = WebDriverWait(driver, 3600) #sec
while(1): #ページの読み込みタイミングを知りたい
    cur_url = driver.current_url    
    if (cur_url != old_url):
        #time.sleep(6)
        
        #waitload_tag("head", 0)
        #wait_test.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "head")))
        
        driver.execute_script(cancel_css_str)
        
        old_url = cur_url

    time.sleep(0.2) #0.01で15% 0.1で3% 0.2で1.3% 1でcpu0.3%

    #cpu 30%
    #cur_url = driver.current_url
    #isUrl = wait_about_url.until_not(expected_conditions.url_contains(old_url))
    #driver.execute_script(cancel_css_str)


    #pythonのプログラムより/usr/lib/firefoxのほうが重い #u_sleep()
    
    #start = time.time()
    
    #driver.execute_script(cancel_css_str)
    #duration = time.time() - start

    #time.sleep(1)
    #print("duration: " + str(duration))

    #ここで、1回だけ見るときは標準入力からなにか入力されたかどうかチェック
    #そのタイミングでスタート

    #element = driver.find_element_by_id("TxtGetOnStation")
    #element.send_keys(unicode("新宿", 'utf-8')) 直江津
    #driver.execute_script("document.forms[0].elements['PlGetOnStation'].value = '20'")#八戸
    #element = driver.find_element_by_id("TxtGetOffStation")
    #element.send_keys(unicode("白馬", 'utf-8')) 越後湯沢
    #driver.execute_script("document.forms[0].elements['PlGetOffStation'].value = '1'")#上野
    #element = driver.find_element_by_id("BtnVacantSeatInquiry")
    #element.click()
    #driver.execute_script("document.getElementById('BtnVacantSeatInquiry').click()")
    #javascript_click("BtnVacantSeatInquiry")


#600sで時間切れ? sleepないとブラウザ閉じてしまうかも
time.sleep(10000)

#driver.get("http://jr-mars.dyndns.org/view/company/index.php")
#"http://127.0.0.1:60622/hub"
#'4e167f26-dc1d-4f51-a207-f761eaf73c31'
# print(driver.command_executor._url)
# print(driver.session_id)
#time.sleep(5)
#print(driver.current_url)
#time.sleep(5)
#print(driver.current_url)
#time.sleep(5)
#print(driver.current_url)

#beforeHwd = driver.window_handle #Returns the handle of the current window.
#Dim Hwds
#Hwds = driver.window_handles #Returns the handles of all windows within the current session.
#Dim window
#print(len(Hwds))
#beforeHwd = driver.window_handles[0] #Returns the handle of the current window.
#print(beforeHwd)
#for window in Hwds:
#    if window != beforeHwd Then
#        driver.switch_to_window(window)
#        driver.get("https://www.eki-net.com/")
#        print("eki-net")

        #driver.Close
#Set driver = driver.switchToWindow(beforeHwd) 'Switches focus to the specified window.
#driver.get "/tatsuya"

#searchBox = driver.find_element_by_css_selector("#srchtxt") #検索入力ボックスのhtmlを探す
#searchBox.send_keys(unicode("えきねっと", 'utf-8'))
#kensakuBotan = driver.find_element_by_css_selector("#srchbtn") #htmlから検索ボタンを探す
#kensakuBotan.click() #検索ボタンをクリック


