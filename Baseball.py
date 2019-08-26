# 야구게임
# 무한 반복 while
#  사용자 입력을 받기 input()
#  strike, ball 판정
#  사용자 입력한 것, strike, ball 출력 print()
#  임의의 수와 사용자 입력 수 가 같으면 HIT, break if
# ---
import random

# 세 자리 중복 없는 임의의 수 만들기
# r0 = random.randrange(1, 9+1)
# r0 = str(r0)
# r1 = random.randrange(1, 9+1)
# r1 = str(r1)
# r2 = random.randrange(1, 9+1)
# r2 = str(r2)
# computer = r0 + r1 + r2
computer = str(random.randrange(100, 999+1))
# l = list(range(1, 9+1)) # [1, 2, ,3 , 4, 5, 6, 7, 8, 9]
# random.shuffle(l)
# l[:3] # 중복 없는 list 3자리 뽑기
# a = ""
# for i in l[:3]:
#   a += str(i) //22, 23, 24 줄이 27 줄이랑 같은 말

l = random.sample(range(1, 9+1), 3)
computer = ''.join(str(i) for i in l[:3])
print(computer)


# computer = "851"
while True:
  player = input("숫자 세자리 입력 : ")
  strike = 0
  ball = 0
  # strike, ball 판정
  for i in range(len(computer)):
    for j in range(len(player)):
      if computer[i] == player[j]:
        if i == j:
          strike += 1
        else:
          ball += 1
  print("{}\tstrike : {}\tball : {}".format(player, strike, ball))
  if computer == player:
    print("HIT")
    break