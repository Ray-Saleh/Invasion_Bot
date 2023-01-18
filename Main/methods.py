from asyncio import TimerHandle
import pyautogui
import time
import win32api, win32con
import win32gui
import os
import mouse
import pytesseract
import cv2
def check_rift():
     if pyautogui.locateOnScreen('rift.png', confidence=0.8, region=(0,0,700,1100)) != None:
        x, y = pyautogui.locateCenterOnScreen('rift.png', confidence=0.8, region=(0,0,700,1100))
        pyautogui.click(x,y)

def checkLogIn():
    if pyautogui.locateOnScreen('login.png', confidence=0.8, region=(0,0,700,1100)) != None:
        os.system("TASKKILL /F /IM HD-Player.exe")
        print("exiting, reopnening in 10s")
        time.sleep(10)

def check_for_daily():
    if pyautogui.locateOnScreen('daily.png', confidence=0.7, region=(0,0,700,1100)) != None:
            click(460,960)
            time.sleep(3)
            click(460,960)


    else:
        check_for_back()

# def check_if_on_HS():
#     if pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100)) != None:
#         os.system("TASKKILL /F /IM HD-Player.exe")
#         print("exiting reopening in 10s")
#         time.sleep(10)
    # else:
    #     print("Not on HS")
def check_for_back():
    while pyautogui.locateOnScreen('back.png', confidence=0.8, region=(0,0,700,1100)) != None:
        click(34,60)
        time.sleep(1)

def check_for_csBACK():
    while pyautogui.locateOnScreen('csBack.png', confidence = .8, region=(0,0,700,1100)) != None:
        click(21,81)
        time.sleep(1)



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_help_if_found():
    if pyautogui.locateOnScreen('help.png', confidence=0.7, region=(0,0,700,1100)) != None: 
        click(540,765)
        print("helping guild members")
        time.sleep(1)
    else:
        print("no help request")

def check_for_disconnect():
    if pyautogui.locateOnScreen('disconnect_ok.png', confidence=0.9, region=(0,0,700,1100)) != None: 
        x, y = pyautogui.locateCenterOnScreen('disconnect_ok.png', confidence=0.9, region=(0,0,700,1100))
        pyautogui.click(x,y)

def startGame():
    os.startfile(r"D:\Program Files\Nox\bin\Nox.exe")
    #if  pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100)) != None:
    #    x, y =pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100))
    #    pyautogui.click(x,y)

    time.sleep(15)
    if  pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100)) != None:
        x, y =pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100))
        pyautogui.click(x,y)

def resizeWindow():
    try: 
        nox = win32gui.FindWindow(None, "not Ray")
        #hwnd = win32gui.FindWindow(None, "BlueStacks")
        win32gui.MoveWindow(nox, 0, 0, 590, 1025, True) #nox player
        #win32gui.MoveWindow(hwnd, 0, 0, 592, 980, True) #bluestacks

        #print("resizing Window")
    except:
        print("window isnt open")
        startGame()
        pass

def click(x,y):
    # x = x-x/5 #-20% for click
    # y = y-y/5
    # x = int(x)
    # y = int(y)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


def check_for_rift():
    if pyautogui.locateOnScreen('rift.png', confidence=0.7, region=(0,0,700,1100)) != None:
        x, y = pyautogui.locateCenterOnScreen('close_rift.png', confidence=0.7, region=(0,0,700,1100))
        pyautogui.click(x,y)


def check_for_zvz():
    if pyautogui.locateOnScreen('zvz.png', confidence=0.9) != None:
        x, y = pyautogui.locateCenterOnScreen('close_zvz.png', confidence=0.7, region=(0,0,700,1100))
        pyautogui.click(x,y)

# ! doesnt work 
def findCashSet(level):
    #locate cash tile
    click(469,990)
    time.sleep(1)
    click(533,454)
    time.sleep(0.5)
    click(533,600)
    time.sleep(0.5)
    click(533,760)
    time.sleep(0.5)
    pyautogui.keyDown(level)
    time.sleep(0.1)
    pyautogui.keyUp(level)
    time.sleep(0.5)
    click(533,760) 
    time.sleep(0.5)
    click(330,830)
# ! doesnt work 
def findCash():
    click(469,990)
    time.sleep(2)
    click(330,830)
    time.sleep(2)
# ! doesnt work
def sendGather():
    time.sleep(2)
    click(350,600)
    time.sleep(1)
    click(350,760)
    time.sleep(1)
    click(500,1180)
    check_for_back()
    
# TODO make this work
def rebels():
    
    if pyautogui.locateOnScreen('Base.png', confidence=0.9, region=(0,0,700,1100)) == None:
        click(88,1162)
        print("not on map, switching...")
        time.sleep(4)
    a = 0
    try:
        while a < 6:
            if pyautogui.locateOnScreen('rebels.png', confidence=0.9, region=(0,0,700,1100)) != None:
                x, y = pyautogui.locateCenterOnScreen('rebels.png', confidence=0.9)
                pyautogui.click(x,y)
                time.sleep(1)
                if pyautogui.locateOnScreen('AP.png', confidence=0.9, region=(0,0,700,1100)) != None:
                    click(204,665)
                    time.sleep(0.2)
                    click(404,730)
                    time.sleep(0.2)
                    click(404,730)
                    time.sleep(0.5)
                    click(330,1100)
                    time.sleep(0.2)
                    a = a + 1 
                    check_for_back()
                else:
                    a = 7 
                    check_for_back()
            else:
                    a = 7
    except:
        pass


def cs_message():
    if pyautogui.locateOnScreen('cs_message.png', confidence=0.8, region=(0,0,700,1100)) != None:
        x, y = pyautogui.locateCenterOnScreen('cs_message.png', confidence=0.7, region=(0,0,700,1100))
        time.sleep(1)
        pyautogui.click(x,y)
#! hAAAAAAAAa
# TODO make this work 
#check if on map, if not bring on map 
def gathering():
    counter = 0
    times = 0
    if pyautogui.locateOnScreen('Base.png', confidence=0.9, region=(0,0,700,1100)) == None:
        click(88,1162)
        print("not on map, switching...")
        time.sleep(4)

    #check if already gathering
    #counter for how often all marches are out is returned
    #times for how many marches have been sent ( or tried to send) 

    while times <7:
    
        if  pyautogui.locateOnScreen('7outof7.png', confidence=0.7, region=(0,0,700,1100)) != None: 
            print ("all marches out")
            times = 7
            
    
        else:
            print("vacant marches, gathering...")
            print(times)
            check_for_back()
            findCash()
            sendGather()
            time.sleep(2)
            times = times + 1
            check_for_back()

    times = 0
    counter = 0
# ! doesnt work 
def hit_zombie():
    if pyautogui.locateOnScreen('Base.png', confidence=0.9, region=(0,0,700,1100)) != None:
        click(88,1162)
        print("on map, switching...")
        time.sleep(4)
    if pyautogui.locateOnScreen('zombie.png', confidence=0.8, region=(0,0,700,1100)) != None:
        click(640,480)
        time.sleep(2)
   # if pyautogui.locateOnScreen('5_hit.png', confidence=0.8) == None:
    #    click(470,1128)
        if pyautogui.locateOnScreen('zombie_energy.png', confidence=0.8, region=(0,0,700,1100)) != None:
            click(350,560)
        else:
            check_for_back()
        check_for_back()

def facebook():
    if pyautogui.locateOnScreen('facebook.png', confidence=0.7, region=(0,0,700,1100)) != None:
        x, y = pyautogui.locateCenterOnScreen('facebook.png', confidence=0.7, region=(0,0,700,1100))
        pyautogui.click(x,y+200)
# TODO make this work
def check_gvg():
    if pyautogui.locateOnScreen('gvg.png', confidence=0.9, region=(0,0,700,1100)):
        x,y = pyautogui.locateCenterOnScreen('gvg.png', confidence=0.9, region=(0,0,700,1100))
        pyautogui.click(x,y)

def check_crash():
    if pyautogui.locateOnScreen('crash.png', confidence=0.8, region=(0,0,700,1100)):
        x,y = pyautogui.locateCenterOnScreen('crash.png', confidence=0.8, region=(0,0,700,1100))
        pyautogui.click(x,y)
        time.sleep(15)
        log_out_if_logged_in()

def check_for_pop_ups():

    for y in range (2):
        check_crash()
        check_restartGame()
        check_browser()
        check_for_csBACK()
        check_for_Discord()
        check_googleStore()
        check_for_zvz()
        check_for_daily()
        check_for_rift()
        checkLogIn()
        check_for_disconnect()
        cs_message()
        facebook()
        check_for_daily()
        check_for_PrivacyPolicy()
        check_for_offer()

def check_for_pop_ups_lite():

    for y in range (2):
        
        #check_for_daily()
        #check_for_rift()
        #checkLogIn()
        check_for_disconnect()
        check_for_Discord()
        cs_message()
        facebook()
        #check_for_daily()
        #check_for_PrivacyPolicy()
        #check_for_offer()

def check_for_offer():
    if pyautogui.locateOnScreen('close_offer.png',confidence=0.8, region=(0,0,700,1100)):
        try:
            x, y = pyautogui.locateCenterOnScreen('close_offer.png',confidence=0.8, region=(0,0,700,1100))
            click(x, y)
        except:
            pass

def scroll_down():
    cs_message()
    check_crash()
    log_out_if_logged_in()
    historical()
    mouse.drag(300, 800, 300, 600, absolute=True, duration=0.6)

def scroll_up():
    check_crash()
    log_out_if_logged_in()
    historical()
    mouse.drag(300, 600, 300, 800, absolute=True, duration=0.6)

def historical():
    if pyautogui.locateOnScreen('historical.png', confidence=0.95) != None:
        x, y = pyautogui.locateCenterOnScreen ('historical.png', confidence=0.9, region=(0,0,700,1100))
        pyautogui.click(x,y)
        time.sleep(2)

def log_into_account(farm_number):
    cs_message()
    historical()
    cs_message()
    logged_in = False
    timera = 0
    while logged_in == False:
        while pyautogui.locateOnScreen('Farm' + farm_number + '/name.png', confidence=0.7, region=(0,0,700,1100)) == None:
            if timera < 14:
                timera = timera +1
                check_for_pop_ups() 
                historical()
                scroll_down()
                time.sleep(3)
            else:
                scroll_up()
                check_for_pop_ups()
                time.sleep(3)
        else:
            x, y = pyautogui.locateCenterOnScreen('Farm'+ farm_number +'/name.png', confidence=0.7, region=(0,0,700,1100))
            print("found account, logging in")
            pyautogui.click(x,y)
            timera =0
            logged_in = True
            time.sleep(4)
            click(337,930)
            time.sleep(10)
            check_for_pop_ups()

def log_out_if_logged_in():
    check_for_pop_ups_lite()
    time.sleep(.2)
    if pyautogui.locateOnScreen('more.png', confidence=0.8, region=(0,0,700,1100)) != None:
        click(520,960)
        time.sleep(2)
        check_for_pop_ups_lite()
        if pyautogui.locateCenterOnScreen('account.png', confidence=0.8, region=(0,0,700,1100)) != None:
            x,y=pyautogui.locateCenterOnScreen('account.png', confidence=0.8, region=(0,0,700,1100))
            click(x,y)
            time.sleep(2)
            check_for_pop_ups_lite()
            if pyautogui.locateCenterOnScreen('log_out.png', confidence=0.8, region=(0,0,700,1100)) !=None:
                click(385,970)
                print("logged out.")
                time.sleep(10)
    
def check_if_on_map():
    check_for_pop_ups()
    if pyautogui.locateOnScreen('Base.png', confidence=0.9, region=(0,0,700,1100)) == None:
        cs_message()
        click(81,969)
        print("not on map, switching...")
        time.sleep(4)

def bring_on_base_screen():
    check_for_pop_ups()
    if pyautogui.locateOnScreen('Base.png', confidence=0.9, region=(0,0,700,1100)) != None:
        cs_message()
        click(81,969)
        print("on map, switching...")
        time.sleep(4)

# ! using harvest_skill2
def harvest_skill():
    if pyautogui.locateOnScreen('Base.png', confidence=0.9, region=(0,0,700,1100)) == None:
        click(81,969)
        print("not on map, switching...")
        time.sleep(4)
    if pyautogui.locateOnScreen('harvest_skill.png', confidence=0.8, region=(0,0,700,1100)) != None:
        x,y = pyautogui.locateCenterOnScreen('harvest_skill.png', confidence=0.8, region=(0,0,700,1100))
        print("using harvest skill")
        pyautogui.click(x,y)
        time.sleep(0.7)
        click(333,744)
        time.sleep(0.4)
        click(40,980)
        time.sleep(3)
    else:
        print("harvest not available")

def check_restartGame():
    if pyautogui.locateOnScreen('restartGame.png', confidence = .9, region=(0,0,700,1000)):
        click(278,615)
        time.sleep(1)
        
def harvest_skill2():
    if pyautogui.locateOnScreen('Base.png', confidence=0.9, region=(0,0,700,1100)) == None:
        click(70,970)
        print("not on map, switching...")
        time.sleep(4)
    click(30,830)
    time.sleep(1)
    click(280,621)
    time.sleep(1)
    click(30,830)

def camera_on_bank():
    cs_message()
    check_if_on_map()
    click(120,85)
    time.sleep(0.5)
    click(120,85)
    time.sleep(0.5)
    click(485,195)
    time.sleep(1)

def trade_interface():
    cs_message()
    click(290,530)
    time.sleep(1)
    click(150,710)

def check_for_PrivacyPolicy():
    if pyautogui.locateOnScreen('pp.png', confidence=0.8, grayscale=True,region=(0,0,700,1100)):
        os.system("TASKKILL /F /IM HD-Player.exe")
        print("exiting reopening in 10s")
        time.sleep(10)
        startGame()
# ! deprecated method do not use

#def Check_Under_different_account():
#        if pyautogui.locateOnScreen('AppStore.png', confidence = .7, region=(0,0,700,1000)):
#            click(270,604)
#            if  pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100)) != None:
#                x, y =pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100))
#                pyautogui.click(x,y)

def check_for_Discord():
    if pyautogui.locateOnScreen('discord_link.png', confidence = .9, region=(0,0,700,1000)):
        click(566,963)
        if  pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100)) != None:
            x, y =pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100))
            pyautogui.click(x,y)

def check_browser():
    if pyautogui.locateOnScreen('check_browser.png', confidence = .9, region=(0,0,700,1000)):
        click(566,963)
        if  pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100)) != None:
            x, y =pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100))
            pyautogui.click(x,y)


def check_googleStore():
    if pyautogui.locateOnScreen('AppStore.png', confidence = .9, region=(0,0,700,1000)):
        click(566,963)
        if  pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100)) != None:
            x, y =pyautogui.locateOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100))
            pyautogui.click(x,y)

def check_rss_amount():
    print("reading energy")
    energySS = pyautogui.screenshot( 'energy.png' , region=(40,100, 60, 30))
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread('energy.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    b = (pytesseract.image_to_string(img))
    print(b)
    cv2.imshow('result',img)
    cv2.waitKey(0)
    

    print(b[-2])

def get_rss_type():
#    time.sleep(1)
#    if pyautogui.locateOnScreen('btest.png', confidence=0.9, region=(0,0,700,140)) != None:
#        #print("see rss over 1m")
#        x,y = pyautogui.locateCenterOnScreen('btest.png', confidence=0.9, region=(0,0,700,140))
#        click(x,y)
#        rsstype = 0
#        if x < 120:
#            rsstype = 1 
#        if 120 < x < 226:
#            rsstype = 2 
#        if 226 < x < 330:
#            rsstype = 3
#        if 330 < x < 470:
#            rsstype = 4
#        if x > 470:
#            rsstype = 5
#        #print(rsstype)
#        match rsstype:
#                case 0: 
#                    print("no rss over 1 bill found")
#                case 1:
#                  print("transferring energy")
#                case 2:
#                    print("transferring oil")
#                case 3:
#                    print("transferring steel")
#                case 4:
#                    print("transferring food")
#                case 5:
#                    print("transferring cash")
#     */   return(rsstype)

    if pyautogui.locateOnScreen('mtest.png', confidence=0.7, region=(0,0,700,140)) != None:
        #print("see rss over 1m")
        x,y = pyautogui.locateCenterOnScreen('mtest.png', confidence=0.6, region=(0,0,700,140))
        click(x,y)
        rsstype = 0
        if x < 120:
            rsstype = 1 
        if 120 < x < 226:
            rsstype = 2 
        if 226 < x < 330:
            rsstype = 3
        if 330 < x < 470:
            rsstype = 4
        if x > 470:
            rsstype = 5
        #print(rsstype)
        match rsstype:
                case 0: 
                    print("no rss over 1 mil found")
                case 1:
                    print("transferring energy")
                case 2:
                    print("transferring oil")
                case 3:
                    print("transferring steel")
                case 4:
                    print("transferring food")
                case 5:
                    print("transferring cash")
        return(rsstype)
    else:
        check_for_back()
        log_out_if_logged_in()
    
def trade_rss():
    if pyautogui.locateOnScreen('taxrate.png', confidence=0.7, region=(0,0,700,1100)):
        if get_rss_type() != None:
            rss = get_rss_type()
            x = 480
            y = 0
            match rss:
                case 0: 
                    print("no rss over 1 mil found")
                case 1:
                    y = 390
                case 2:
                    y = 500
                case 3:
                    y = 610
                case 4:
                    y = 270
                case 5:
                    y = 720
            #click(x, y)
            time.sleep(0.5)
            click(x, y)
            time.sleep(0.5)
            pyautogui.keyDown('9')
            for i in range (9):
                time.sleep(0.01)
                pyautogui.keyDown('9')
            click(280,980)
            time.sleep(1)
            click(280,980)
            time.sleep(0.5)
    else:
        camera_on_bank()
        trade_interface()

def harvest_plan():
    click(30,440) # open plan menu
    time.sleep(1.5)
    click(274,100) # switch to plan side
    time.sleep(0.5)
    click(274,170) # click harvest plan 
    time.sleep(0.5)
    click(140,980) # clic k execute 
    time.sleep(0.5)
    click(400,600) # click done 
    
    time.sleep(0.5)
    click(274,170) # click harvest plan 
# start fomulating plan 
    time.sleep(0.2)
    click(424,985) # click formulate
    time.sleep(1)
    fff = 0
    while pyautogui.locateOnScreen('morerss.png',confidence=0.9, region=(0,0,700,1100)) and fff < 4:
        x,y = pyautogui.locateCenterOnScreen('morerss.png',confidence=0.9, region=(0,0,700,1100))
        click(x,y)
        fff = fff + 1
        time.sleep(1)
        if pyautogui.locateOnScreen('preview.png',confidence=0.9, region=(0,0,700,1100)):
            x,y = pyautogui.locateCenterOnScreen('preview.png',confidence=0.9, region=(0,0,700,1100))
            click(x,y)
            time.sleep(1)
            click(415,835) # lick use 
            time.sleep(1)
            click(50,50)
            time.sleep(1)
        time.sleep(1)
    click(260,990) # click formulate final 
    time.sleep(1)
    print("Harvest plan complete.")
    check_for_back()
   
def rewards():
    if pyautogui.locateOnScreen('Base.png', confidence=0.9, region=(0,0,700,1100)) == None:
        
        if pyautogui.locateOnScreen('rewards_center.png',confidence=0.7):
            
            click(22,700) #open rewards centre 
            time.sleep(0.5)
            click(270,980) # claim all 
            time.sleep(0.5)
            click(414,612) # Yes
            check_for_back()

def open_to_dos():
    click(530,810) #opens todo screen

def tesla():
    times_clicked = 0
    bring_on_base_screen()
    open_to_dos()
    time.sleep(1)
    #find tesla button 
    if pyautogui.locateOnScreen('tesla_todo.png',confidence=0.9, region=(0,0,600,1100)) != None:
        print("see it")
        x, y = pyautogui.locateCenterOnScreen('tesla_todo.png',confidence=0.9, region=(0,0,600,1100))
        click(x,y)
        time.sleep(0.5)
    click(470,670) # click develop to get speedups
    while times_clicked < 7:
        pyautogui.click(290,640) #develop
        time.sleep(1)
        click(470,210)
        time.sleep(0.2)
        click(470,210)
        time.sleep(0.1)
        click(470,210)
        time.sleep(0.5)
        click(470,670) # click develop to get speedups

        click(290,640) #
        time.sleep(0.5)
        times_clicked = times_clicked + 1
    check_for_back()




# if  pyautogui.locateOnScreen('appcover.png', confidence=0.7, region=(0,0,700,1100)) != None:
#         x, y =pyautogui.locateCenterOnScreen('appcover.png', confidence=0.8, region=(0,0,700,1100))
#         pyautogui.click(x,y)
#         print("see")

#def Progress_not_under_This_account():
#    if pyautogui.locateOnScreen('progress_not_under_this_account.png', confidence = .8, region= (0,0,700,1100), greyscale = True):
