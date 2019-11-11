import Result

class Question:
    # __init__함수로 생성자를 만듦 (gi, jung, gun에 값을 더하고 저장해놓아야 하므로, 0으로 초기화)
    def __init__(self):
        self.skinType = ""
        self.gi = 0
        self.jung = 0
        self.gun = 0

    # 질문을 하기 위해서 사용하는 함수
    def question(self):
        q1 = input("1.모공의 크기를 선택해주세요.(0 : 작은 편, 1 : 보통, 2 : 큰 편)")
        if q1 == "0":
            self.gun += 1 # 0에 해당하는 것이 건성의 특징이므로 0을 입력하면 gun에 하나를 더하기
        elif q1 == "1":
            self.jung += 1 # 0에 해당하는 것이 중성의 특징이므로 0을 입력하면 jung에 하나를 더하기
        elif q1 == "2":
            self.gi += 1 # 0에 해당하는 것이 지성의 특징이므로 0을 입력하면 gi에 하나를 더하기

        q2 = input("2. 눈가의 잔주름 상태를 선택해주세요.(0 : 많음, 1 : 약간 있음, 2 : 적음)")
        if q1 == "0":
            self.gun += 1
        elif q1 == "1":
            self.jung += 1
        elif q1 == "2":
            self.gi += 1

        q3 = input("3. 세안 후 피부의 당김 정도를 선택해주세요.(0 : 많이 당김, 1 : 약간 당김, 2 : 안당김)")
        if q1 == "0":
            self.gun += 1
        elif q1 == "1":
            self.jung += 1
        elif q1 == "2":
            self.gi += 1

        q4 = input("4. 얼굴이 붉어지는 정도를 선택해주세요.(0 : 자주 붉어짐, 1 : 종종 붉어짐, 2 : 거의 안붉어짐)")
        if q1 == "0":
            self.gun += 1
        elif q1 == "1":
            self.jung += 1
        elif q1 == "2":
            self.gi += 1

        q5 = input("5. 학창시절 트러블의 정도를 선택해주세요.(0 : 거의 안생김, 1 : 가끔 생김, 2 : 자주 생김)")
        if q1 == "0":
            self.gun += 1
        elif q1 == "1":
            self.jung += 1
        elif q1 == "2":
            self.gi += 1

        q6 = input("6. 샴푸 후 모발이 기름지는 시점을 선택해주세요.(0 : 샴푸를 하고 약 3일 후, 1 : 샴푸한 다음 날, 2 : 샴푸한 당일 오후)")
        if q1 == "0":
            self.gun += 1
        elif q1 == "1":
            self.jung += 1
        elif q1 == "2":
            self.gi += 1

        if self.gun > self.gi and self.gun > self.jung: # gi와 jung의 갯수보다 gun의 갯수가 많으면 skinType에 건성을 저장
            self.skinType = "건성"
        elif self.jung >= self.gun and self.jung > self.gi and self.gi == self.gun: # gun보다 jung의 갯수가 많거나 같고, gi의 갯수보다 많고, gi와 gun의 갯수가 같으면 skinType에 중성을 저장
            self.skinType = "중성"
        elif self.gi > self.gun and self.gi > self.jung: # gun과 jung의 갯수보다 gi의 갯수가 많으면 skinType에 지성을 저장
            self.skinType = "지성"

        print("\n")
        print("-----------------------------------------------------------------------------------------------------")
        print("\n")
        print("피부 타입 : " + self.skinType) # 건성, 중성, 지성 중 skinType에 있는 값을 출력