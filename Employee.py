#p.200

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def eat(self, food):
    print(self.name + "이/가 " + food + "을/를 먹습니다.")

  def __str__(self):
    return self.name + "은/는 " + str(self.age) + "살 입니다."

class Employee(Person):
  def __init__(self, name, age, salary):
    super().__init__(name, age) # 부모 생성자 가져오는 방법 !
    self.salary = salary

  def work(self):
    print("일 합니다.")

  def get_salary(self):
    print("급료를 받습니다.")
    return self.salary

e = Employee("서남경", 18, 300)
print(e)
e.eat("밥")
e.work()
r = e.get_salary()
print("급료는 " + str(r) + "만 원입니다.")
  