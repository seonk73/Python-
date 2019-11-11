import Question
import PastResult
import sys

class FirstScreen:
  # 프로그램을 시작할 때 나타나는 질문과 파일에 저장해두었던 결과를 볼 것인지 물어보는 질문을 처리하는 함수
  def start(self):
      s = input("피부 타입 설문을 시작하시겠습니까? (Y/N) : ")
      if s == "Y" or s == "y":
          self.q = Question.Question()
          self.q.question()
          self.isPrint = True # True일 때만 출력 O

      else:
          self.isPrint = False # False이면 출력 X
          s1 = input("이전 결과를 보시겠습니까? (Y/N) : ")
          if s1 == "Y" or s1 == "y":
              self.p = PastResult.PastResult() # 파일에서 이전 결과 가져와서 띄우기
              self.p.file()
          else:
              sys.exit()  # 전체 프로그램에서 탈출