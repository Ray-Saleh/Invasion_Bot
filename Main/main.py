from cv2 import log
from methods import *
import pyautogui
import time
import keyboard
import random




def main():
        lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26] # ! change amount of farms here
        #random.shuffle(lst)
        round = 0
        for number in lst:
                round += 1
                skill = 0
                resizeWindow()
                check_for_pop_ups()
                log_out_if_logged_in()
                print("round: ",round)
                print("doing farm number:", number)
                resizeWindow()
                log_out_if_logged_in()
                check_crash()
                log_into_account(str(number))
                time.sleep(5)
                check_crash()
                rewards()
                rewards()
                #tesla()
                check_if_on_map()
                check_for_back()
                harvest_skill2()
                time.sleep(0.5)
                #harvest_plan()
                check_for_back()
                camera_on_bank()

                #trade billion  /// if not trading rss in billions turn off
              #  while pyautogui.locateOnScreen('b_small.png', confidence=0.7, region=(0,0,700,140)) != None:
              #      if skill == 0:
              #          #harvest_skill2()
              #          skill = 1
              #      print("Trading B")
              #      trade_rss()
              #      time.sleep(2)

                
                while pyautogui.locateOnScreen('m_small.png', confidence=0.7, region=(0,0,700,140)) != None:
                    if skill == 0:
                        harvest_skill2()
                        skill = 1
                    trade_rss()
                    time.sleep(1)

How_manyTimes = 0
while True:
    print("starting...")
    check_for_pop_ups()
    resizeWindow()
    resizeWindow()
    log_out_if_logged_in()
    check_for_pop_ups()
    resizeWindow()
    main()
    check_for_back()
    log_out_if_logged_in()
    print("done")
    How_manyTimes += 1
    print("Looped:", How_manyTimes)



