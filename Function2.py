#p.107~112
import random
# def rolling_dice():
#   n = random.randint(1, 6) #1<=n<=6 랜덤 숫자 (randrange는 1~5까지, randint는 1~6까지)
#   print("6면 주사위를 굴린 결과 : ", n)
# def rolling_dice(pip):
#   n = random.randint(1, pip) #1<=n<=pip 랜덤 숫자 (randrange는 1~5까지, randint는 1~6까지)
#   print(pip, "면 주사위를 굴린 결과 : ", n)
def rolling_dice(pip, repeat):
  for r in range(1, repeat+1):
    n = random.randint(1, pip) #1<=n<=pip 랜덤 숫자 (randrange는 1~5까지, randint는 1~6까지)
    print(pip, "면 주사위를 굴린 결과", r, " : ", n)

rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(3, 0)

#p.109
def star():
  print("*****")

star() #*****
star() #*****
star() #*****

#p.113
print("♥")
print("♥", "♪")
print("♥", "♪", "♣")
print("♥", "♪", "♣", "♠")
print("♥", "♪", "♣", "♠", "★")

#p.114
# def p(*args): # *이 붙는 것이 중요함
#   string=""
#   for a in args:
#     string += " "+a 
#   print(string.strip())

# p("♥")
# p("♥", "♪")
# p("♥", "♪", "♣")
# p("♥", "♪", "♣", "♠")
# p("♥", "♪", "♣", "♠", "★")

#p.114
def p(space, space_num, *args):
  string = args[0] #index로 접근이 가능
  for i in range(1, len(args)):
    string += (space * space_num) + args[i]
  print(string)

p(",", 3, "♥", "♪")
p("★", 2, "♥", "♪", "♣")
p("_", 3, "♥", "♪", "♣", "♠")

#P.115
def star2(ch, *nums):
  # for i in range(len(nums)):
  #   print(ch * nums[i])
  for n in nums:
    print(ch * n)

star2("♪", 3)
star2("♥", 1, 2, 3)

#p.116
def fn(a, b, c, d, e):
  print(a, b, c, d, e)

fn(1, 2, 3, 4, 5)
fn(10, 20, 30, 40, 50)
fn(a=1, b=2, c=3, d=4, e=5)
fn(e=5, d=4, c=3, b=2, a=1)
fn(1, 2, c=3, d=4, e=5)
# fn(d=4, e=5, 1, 2, 3) #error

#p.118
# ***__***
# ***__***
# ***__***

def star3(mark, repeat, space, space_repeat, line):
  for _ in range(line):
    string = (mark * repeat) + (space * space_repeat) + (mark * repeat)
    print(string)

star3("*", 3, "_", 2, 3)

#p.119
def hello(msg="안녕하세요"):
  print(msg + "!")

hello("안녕")
hello("안 녕")
hello()

#p.120
def hello2(name, msg="안녕하세요"):
  print(name + "님, " + msg + "!")

hello2("서남경", "반가워욤")
hello2("서남경")
# hello2() #error, name의 인자가 없음

def fn2(a, b=[]):
  b.append(a)
  print(b)

  fn2(3)  #[].append(3) -> [3]
  fn2(5)  #[].append(5) -> [5] : x -> [3, 5] : o #list는 함수가 살아있는동안 그 전의 값을 가지고 있음. 일반 변수는 현재 값으로 대체가 됨
  fn2(10) #[3, 5, 10]
  fn2(7, [1]) #[3, 5, 10, 1, 7] : x vs [1, 7] : o
  # fn2(a=7, b=[1]):
  #   print([1].append(7))

 #p.123

def gugudan(dan=2):
  for i in range(1, 9+1, 1):
    print(dan, "X", i, "=", dan*i)

gugudan(3)
gugudan(2)
gugudan()

#p.125

def sum(*numbers):
  sum_value = 0
  for number in numbers:
    sum_value += number

  return sum_value

print("1 + 3 = ", sum(1, 3))
print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))

def min(*numbers):
  min_value = numbers[0]
  for number in numbers:
    if min_value > number:
      min_value = number
  return min_value

print("min(3, 6, -2) = ", min(3, 6, -2))

def max(*numbers):
  max_value = numbers[0]
  for number in numbers:
    if max_value < number:
      max_value = number
  return max_value

print("max(8, 1, -1, 12) =", max(8, 1, -1, 12))

def multi_num(multi, start, end):
  result = []
  for n in range(start, end):
    if n % multi == 0:
      result.append(n)
  return result

print("multi_num(17, 1, 100) = ", multi_num(17, 1, 100))
print("multi_num(3, 1, 200) = ", multi_num(3, 1, 200))

def min_max(*args):
  min_value = args[0]
  max_value = args[0]
  for a in args:
    if min_value > a:
      min_value = a
    if max_value < a:
      max_value = a
  return min_value, max_value

min, max = min_max*(52, -3, 23, 90, -23)
print("최솟값 : ", min, "최댓값 : ", max)

