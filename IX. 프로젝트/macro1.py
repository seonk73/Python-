import pyautogui as pag

if __name__ == '__main__':
    pag.moveTo(614, 533, duration=2)    # 2는 속도 / 절대적 위치
    # pag.click()
    # pag.click()
    # pag.click(clicks=2)
    # pag.doubleClick()
    # pag.move(100, 200, duration=1)  # 자기 위치에서 좌표만큼 이동 (상대적 위치)
    # pag.rightClick()
    # pag.click(button="right")
    pag.drag(0, 200, duration=2)