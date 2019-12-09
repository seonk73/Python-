import pyautogui as pag
import time

if __name__ == '__main__':
    # 메모장 프로그램 실행하기
    pag.moveTo(214, 1072, 2)
    pag.click()
    pag.press("hangul")
    pag.typewrite("apahwkd")
    pag.press("enter")
    pag.moveTo(200, 200, 2)
    pag.click()
    # hello world 치기
    pag.typewrite("hello world")
    # enter 두 번 치기
    pag.press("enter")
    pag.press("enter")
    pag.press("hangul")
    # 반갑구나 세상아 치기
    pag.typewrite("qksrkqrnsk tptkddk")
    # 저장하기
    pag.hotkey('ctrl', 's')     # pag.keyDown('ctrl')
                                 # pag.press('s')
                                 # pag.keyUp('ctrl')
    time.sleep(1)
    # 파일이름  : 파이썬월드
    # pag.typewrite("C:\\Users\\s2018\\Downloads")
    # pag.press("hangul")
    pag.typewrite("vkdlTjsdnjfem")
    pag.press("enter")