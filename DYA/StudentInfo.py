class StudentInfo: 
  # __init__함수로 생성자를 만들어 학년, 학급, 번호를 입력할 수 있게 만듦
  def __init__(self): 
    self.grade = input("학년을 입력해주세요 : ")
    self.classes = input("학급을 입력해주세요 : ")
    self.number = input("번호를 입력해주세요 : ")