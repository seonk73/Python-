#p.195

class Car:
  count = 0                     # Car.count 쓰면 X

  def __init__(self, type, speed):
    self.type = type
    self.speed = speed
    Car.count += 1              # count만 쓰면 X

  @classmethod                  # 반드시 있어야함
  def get_count(cls):           # 꼭 이름이 cls가 아니어도 됨
      return cls.count          # Car.count 써도 됨

  def move(self):
    print(self.type + "가" + str(self.speed) + " 속도로 움직입니다.")

  def speed_up(self, amount):
    self.speed += amount

  def speed_down(self, amount):
    self.speed -= amount

print(Car.get_count())
c = Car("스포츠카", 200)
c.speed_up(10)
c.move() # move는 함수이므로 괄호 넣어주기
c.speed_down(10)
c.move()

d = Car("테슬라", 200)
d.speed_up(50)
d.move()
d.speed_down(150)
d.move()
print(Car.get_count())