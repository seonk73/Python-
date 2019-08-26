class AttendInfo:
  # __init__함수로 생성자를 만듦 (출석 여부를 입력받기 위해 attend를 None으로 초기화, 
  #                             출석이 아닌 다른 것을 선택했을 때의 사유를 입력받기 위해 reason은 빈 공간으로 초기화)
  def __init__(self):
    self.attend = None
    self.reason = ""

  # 출석 여부를 물어본 뒤, 대답을 return(만약 지각이면 tardy(), 조퇴면 early(), 결석이면 absent()로 각각 함수를 가리킴)
  def set_ainfo(self):
    self.attend = input("출석 여부를 작성해주세요(ex) 출석, 지각, 조퇴, 결석 중 택 1) : ")
    if self.attend == "지각":
      self.tardy()
    elif self.attend == "조퇴":
      self.early()
    elif self.attend == "결석":
      self.absent()
    return self.attend
      
  # 호출하면 입력한 attend 값을 return
  def get_attend(self):
    return self.attend

  # 출석 여부에서 지각을 입력했을 때 실행되는 함수, 구체적으로 지각 사유를 물어봄)
  def tardy(self):
    self.reason = input("지각 사유를 작성해주세요 (ex)질병, 미인정, 기타, 인정) : ")

  # 출석 여부에서 조퇴를 입력했을 때 실행되는 함수, 구체적으로 조퇴 사유를 물어봄)
  def early(self):
    self.reason = input("조퇴 사유를 작성해주세요 (ex)질병, 미인정, 기타, 인정) : ")

  # 출석 여부에서 결석을 입력했을 때 실행되는 함수, 구체적으로 결석 사유를 물어봄)
  def absent(self):
    self.reason = input("결석 사유를 작성해주세요 (ex)질병, 미인정, 기타, 인정) : ")

  # __str__함수로 attend 값을 문자열화, 
  # 출석이면 그대로 출석 출력, 출석이 아니면 뒤에 괄호를 넣어 괄호 안에 구체적인 사유가 나타나게함
  def __str__(self):
    if self.attend == "출석":
      return "출석"
    else:
      return self.attend+"("+self.reason+")"