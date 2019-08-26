# 문제 : 숫자를 입력받아 각 자릿수의 합 구하기

# 입력받기
number = input()
list = []
sum = 0
# 길이 구하기
length = len(number)

for x in number :
  list += x

for n in range(0,length):
# 숫자로 바꾸기
  sum += int(list[n])
# 더하고 그 값을 출력하기
print(sum)
