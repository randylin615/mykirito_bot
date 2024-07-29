##mykirito_v2.1.py

import time
from selenium import webdriver
import random
from selenium.webdriver.chrome.options import Options
PVP_hcaptcha = 0
life= True

    
# login in google
def login():
    username = ""
    password = ""
    driver.get('https://stackoverflow.com/users/signup')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    driver.find_element_by_id('identifierId').send_keys(username)
    driver.find_element_by_id('identifierNext').click()
    time.sleep(4)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_id('passwordNext').click()

# set cookie to bypass
def hcaptcha_bypass():
    driver.get('https://dashboard.hcaptcha.com/login')
    time.sleep(2)
    driver.find_element_by_id('email').send_keys('@gmail.com')
    driver.find_element_by_id('password').send_keys('')
    driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/div[3]/button').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/button').click()
    time.sleep(2)


# hcaptcha bypass
def hcaptcha():
    global PVP_hcaptcha
    frame = driver.find_element_by_css_selector('iframe[src*="hcaptcha"]')
    time.sleep(2) 
    frame.click()
    print('**************Bypassed**************')
    PVP_hcaptcha = 1
    time.sleep(5) 

        
def activity(floor,num):
    global life
    # initialize variable
    # change  browser title
    if int(num) == 1:
        title = " document.title = '正在執行:狩獵兔肉 V2.1';"
    elif int(num) == 2:
        title = " document.title = '正在執行:自主訓練 V2.1';"
    elif int(num) == 3:
        title = " document.title = '正在執行:外出野餐 V2.1';"
    elif int(num) == 4:
        title = " document.title = '正在執行:汁妹 V2.1';"
    elif int(num) == 5:
        title = " document.title = '正在執行:做善事 V2.1';"
    elif int(num) == 6:
        title = " document.title = '正在執行:坐下休息 V2.1';"
    elif int(num) == 7:
        title = " document.title = '正在執行:釣魚 V2.1';"
    # whether floor bonus
    if (floor == 'y'):
        xpath = '//*[@id="root"]/div/div[2]/div[4]/button[' + str(num) + ']'
    elif (floor == 'n'):
        xpath = '//*[@id="root"]/div/div[2]/div[3]/button[' + str(num) + ']'
    # activity colddown
    sec = random.randint(68, 72)
    # current time
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime)
    print('冷卻秒數：'+ str(sec))
    # life state
    life_state = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]').get_attribute('style')
    if life_state == "opacity: 0;":
        act = driver.find_element_by_xpath(xpath)
    else:   
        life = False
        print("**************角色死亡**************")
    # click
    if act.is_enabled():
        act.click()
        print("**************已行動**************")
        if driver.find_element_by_xpath('//*[@id="actionBar"]').is_enabled():
            print(driver.find_element_by_xpath('//*[@id="actionBar"]').text)
        time.sleep(5)
        driver.refresh()
        driver.execute_script(title)
        time.sleep(sec)
    #  captcha bypass
    else:
        print('**************驗證**************')
        driver.refresh()
        hcaptcha()
        
        
def PVP(PVP_type):
    global PVP_hcaptcha
    global life
    sec = random.randint(173, 178)
    localtime = time.asctime( time.localtime(time.time()) )
    PVP_path = ''
    print(localtime)
    print('冷卻秒數：'+ str(sec))
    life_state = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]').get_attribute('style')
    if (life_state == "opacity: 0;"):
        if driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[3]/button').is_enabled():
            print('**************無驗證或已驗證**************')
            PVP_type = int(PVP_type) + int(PVP_hcaptcha)
            PVP_path = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div[' + str(PVP_type) + ']/button' )
            PVP_hcaptcha = 0
            time.sleep(2)
            PVP_path.click()
            print('**************行動**************')
            time.sleep(3)
            driver.refresh()
            time.sleep(sec) 
        else:
            PVP_type = int(PVP_type) + 1
            driver.refresh()
            hcaptcha() 
    else:
        life = False
        print("**************角色死亡**************")
        
   
     
        
options = Options()
options.add_argument("user-data-dir=C:\selenum\AutomationProfile_copy")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=options)
driver.get("https://mykirito.com")
driver.implicitly_wait(10) 
activity_count = 0

#hcaptcha_bypass()
request = input("請確認要選擇的動作 #行動1 #PVP2  ")
if (request == '1'):
    floor_state = input("請確認是否有樓層獎勵(y/n) 小寫限定  ")
    multi_action = input("請選擇是否要執行多重行動(y/n) 小寫限定  ")
    
    if (multi_action == 'y'):
        multi_data1,multi_data2 = input ("目前僅可選擇2種行動 需搭配油猴插件 升等後會重置計數器 \n請先輸入欲選擇之行動(以空格分開 EX:1 2)\n#兔肉1  #自主2  #野餐3  #汁妹4  #善事5  #坐下6  #釣魚7  ").split()
        multi_data1_timer,multi_data2_timer = input("請分別輸入週期的行動比例(以冒號分隔EX:3:1 先完成3後完成1)  ").split(':')
        multi_data1 = int(multi_data1)
        multi_data2 = int(multi_data2)
        multi_data1_timer = int(multi_data1_timer)
        multi_data2_timer = int(multi_data2_timer)
        driver.get('https://mykirito.com/')
        print('********************************')
        time.sleep(3)
        while (life == True):
            if (activity_count < multi_data1_timer): #3
                action_type = multi_data1
            elif ((activity_count - multi_data1_timer) < multi_data2_timer): #2
                action_type = multi_data2
            activity_count = activity_count + 1
            if (activity_count == 5):
                activity_count = 0
            activity(floor_state,action_type)
        print("腳色死亡 請轉生")
            
    elif (multi_action == 'n'):
        action_type = input("請選擇行動\n#兔肉1  #自主2  #野餐3  #汁妹4  #善事5  #坐下6  #釣魚7  ")
        driver.get('https://mykirito.com/')
        print('********************************')
        time.sleep(3)
        while (life == True):
            activity(floor_state,action_type)
        print("腳色死亡 請轉生")
            
elif (request == '2'):
    driver.get('https://mykirito.com/profile/5efbb9f240f8036820c97020') #喵喵兒ouo
    #driver.get('https://mykirito.com/profile/5efaffbdaafa03283cbfb1e0') #RandyYoo
    #driver.get('https://mykirito.com/profile/5efbbd8341f896682c421528') #瘋狗石頭2號
    PVP_type = input("請輸入要進行的PVP類型 #友切1  #認真2  #決一3  #超渡4  ")
    time.sleep(3)
    PVP_type = int(PVP_type) + 1
    while (life == True):
        PVP(PVP_type)
