import pyautogui as pag
import time     # sleep

if __name__ == '__main__':
    pag.moveTo(200, 200, 2)
    pag.click()
    pag.click()
    pag.typewrite("happy birth day to seungyeon!", interval=0.2)
    pag.press("enter")
    pag.typewrite("happy birth dat to namkyeong!")
    pag.press("hangul")
    pag.typewrite("skaruddk toddlf cnrgkgo!!") # 메모장에 "남경아 생일 축하해!!"라고 나옴
    pag.press("hangul")