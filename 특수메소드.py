class DeletableClass:
  def __del__(self):
    print("delete")

d = DeletableClass()
del d

#p.203
class Person:
  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height

  def __str__(self):
    return "Person 설명, 이름은 "+self.name+" 나이는 "+str(self.age)+" 키는 "+str(self.height)

  def __len__(self):
    return len(self.name)     #self.height -> 키가 출력됨 #len(self.name) -> 이름의 글자 수가 출력됨
    
  def __getitem__(self, key):
    if key == 'name': # 따옴표는 큰거든 작은거든 상관 없음
      return self.name
    if key == 'age':
      return self.age
    return None

p = Person("류정민", 18, 170)
print(p)
print(len(p)) #3
print(p["age"]) #18
print(p["unknown"]) #None