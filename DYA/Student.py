# 2309 서남경
# 프로젝트 소개 : 학교 생활을 하다보면, 수업시간마다 학생들의 출석 여부를 확인하는데요. 
#                매 시간마다 같은 일을 반복하는 번거로움을 조금이나마 해소하기 위해 해당 프로젝트를 생각해보게 되었고,
#                DYA ?를 사용하면 하루 한 번의 체크로 선생님과 학생 모두 간단하게 출결을 관리할 수 있습니다. 


# 다른 파일의 내용을 참조하기 위해 import
import StudentInfo
import ClassInfo
import AttendInfo
import sys # sys.exit를 사용하기 위해

class Item:
  # ClassInfo 파일의 내용을 참조하는 변수를 c, AttendInfo 파일의 내용을 참조하는 변수를 a로 하기 위해 None으로 초기화
  def __init__(self):
    self.c = None
    self.a = None    

  # 앞서 초기화한 변수 c, a에 각각의 class(ClassInfo(), AttendInfo())를 대입,
  # item list에 c, a를 차례로 넣음
  def set_item(self):
    self.c = ClassInfo.ClassInfo()
    result1 = self.c.set_cinfo()
    if result1 == "": # 아무것도 입력하지 않으면 Fals e return, 현재 수업 물어보는 질문 종료
      return False
    self.a = AttendInfo.AttendInfo()
    result2 = self.a.set_ainfo()
    if result2 == "": # 아무것도 입력하지 않으면 False return, 출석 여부 물어보는 질문 종료
      return False   
    self.item = [self.c, self.a]
    return True

  # 호출하면 list로 넣어둔 item을 return
  def get_item(self):
    return self.item

  # __str__함수로 c, a 값을 문자열화
  def __str__(self):
    return self.c + " " + self.a

class Student:  
  # StudentInfo 파일의 내용을 참조하는 변수를 std1로 하여 None으로 초기화, 
  # 입력한 현재 수업과 출석 여부의 값을 가져오기 위해 attend_list를 만들어 빈 list로 초기화
  def __init__(self):
    self.std1 = None
    self.attend_list = []

  # 미림여자정보과학고등학교 학생인지 확인, 맞다면 다음으로 넘어가고, 아니면 곧바로 프로그램 종료
  def mirim(self): 
    m_std = input("미림여자정보과학고등학교 학생이신가요? (Y/N) : ")
    if m_std == "Y" or m_std == "y":
      self.std1 = StudentInfo.StudentInfo()
    else:
      print("해당 프로그램은 미림여자정보과학고등학교에 재학 중인 학생만 사용하실 수 있습니다ㅜ.ㅜ")
      sys.exit() # 그냥 exit -> 해당 함수에서 탈출, sys.exit() -> 전체 프로그램에서 탈출

  # 자신이 앞서 입력한 결과를 확인시켜주기 위해 출력해주는 함수
  def print_info(self):
    print("\n")
    print("==============================================입력 결과==============================================")
    print("\n")
    for item in self.attend_list: # atted_list에 입력된 결과의 수만큼 반복하여(for문 사용) 밑의 print문을 출력
      print("학년 : "+str(self.std1.grade)+"\t학급 : "+str(self.std1.classes)+"\t번호 : "+str(self.std1.number), "\t현수업 : ", item[0], " \t출석 여부 : ", item[1])
      print("\n")
      print("-----------------------------------------------------------------------------------------------------")
      print("\n")

  # i 변수에 Item() class를 대입,
  # while문으로 Item() class의 set_item()을 반복하여 계속 질문(아무것도 입력하지 않고 enter를 치기 전까지)
  def set_item(self):
    i = Item()
    while True:
      made = i.set_item()
      if made == True:
        self.attend_list.append(i.get_item()) # attend_list에 입력한 값을 가지고 있는 get_item()을 호출하여 빈 list에 값 추가하기
      else:
        break

# 실행문들 ----
a = Student()
a.mirim()
a.set_item()
a.print_info()
# ------------

# 입력한 갯수만큼 출석 여부(출석, 지각, 조퇴, 결석 4가지)를 보여주기 위해 각각의 값을 0으로 초기화
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for item in a.attend_list: # 각 출석 여부에 따라 사용자가 입력한 수만큼 1씩 증가
  if item[1].get_attend() == "출석":
    sum1 += 1
  elif item[1].get_attend() == "지각":
    sum2 += 1
  elif item[1].get_attend() == "조퇴":
    sum3 += 1
  elif  item[1].get_attend() == "결석":
    sum4 += 1

# 최종적으로 하루의 출석 현황을 보여줌 (ex) 조퇴 몇 번, 지각 몇 번 등)
print("==============================================출석 현황==============================================")
print("\n")
print("출석 : "+str(sum1)+"번"+"\t지각 : "+str(sum2)+"번"+"\t조퇴 : "+str(sum3)+"번"+"\t결석 : "+str(sum4)+"번")
print("\n")
print("-----------------------------------------------------------------------------------------------------")