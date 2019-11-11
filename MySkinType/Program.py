# 2309 서남경
# 프로젝트 소개 : 자신의 피부 타입을 알지 못하여 자신에게 꼭 맞는 관리를 하지 못하는 사람들을 위해 간단한 설문으로
#                 자신의 피부 타입과 피부 타입에 따른 관리 팁을 알려주는 프로그램(프로젝트)
# 실행 방법 ↓
# -- main 함수가 포함된 해당 파일(Program.java)에서 실행
# -> 피부 타입 설문을 시작하시겠습니까? (Y/N) | Y -> 설문 시작, N -> 프로그램 종료 <Y 선택>
# -> 설문 6개 질문이 끝나면 자신의 피부 타입과 피부 타입에 따른 관리 팁을 보여줌
# -> 결과를 저장하시겠습니까? (Y : 결과 저장 / N : 프로그램 종료) | Y -> 파일에 피부 타입 저장 후 종료, N -> 프로그램 종료 <Y 선택>
# -------- 프로그램 새로 실행
# -- 피부 타입 설문을 시작하시겠습니까? (Y/N) | Y -> 설문 시작, N -> 프로그램 종료 <N 선택>
# -> 이전 결과를 보시겠습니까? (Y/N) | Y -> 이전 설문에서 파일에 저장했던 피부 타입을 보여줌, N -> 프로그램 종료

import FirstScreen
import PastResult
import Question
import Result

class Program:
    # __init__함수로 생성자를 만듦 (si1, si2 변수를 사용하기 위해 None으로 초기화)
    def __init__(self):
        self.si1 = None
        self.si2 = None

    # 콘솔 화면(창)에 순서대로 출력하기 위한 함수
    def print_r(self):
        self.si1 = FirstScreen.FirstScreen()
        self.si1.start()

        if self.si1.isPrint == True: # isPrint가 True일 때만 출력하도록 함
            self.si2 = Result.Result()
            self.si2.print_result(self.si1.q)
            self.si2.end(self.si1.q)

si = Program()
si.print_r()

