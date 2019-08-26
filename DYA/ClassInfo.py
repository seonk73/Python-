class ClassInfo:
  # __init__함수로 생성자를 만듦 (현재 수업을 입력받기 위해 period는 None으로 초기화)
  def __init__(self):
    self.period = None
  
  # 현재 수업을 물어보고, 대답을 return
  def set_cinfo(self):
    self.period = input("현재 수업을 입력해주세요(ex) 조회, 1교시 ~ 7교시, 종례, 방과후 A, 방과후 B) : ")
    return self.period
    
  # __str__함수로 period 값을 문자열화
  def __str__(self):
    return self.period