import random

print("0이상 1미만 실수 값")
print("random.random() : ", random.random())
print()

print("시작값 2.5이상 끝값 10.0 미만 실수 값")
print("random.uniform(2.5, 10.0) : ", random.uniform(2.5, 10.0))
print()

print("0이상 끝값 10미만 정수 값")
print('random.randrange(10) : ', random.randrange(10))
print()

print("1이상 끝값 7미만, 증가 값이 2인 정수 값")
print('random.randrange(1, 7, 2) : ', random.randrange(1, 7, 2)) # 미만이기에 1, 3, 5 중 하나가 뽑힘, 끝값 포함 X
print()

print("1이상 끝값 7이하, 정수 값")
print('random.randint(1, 7) : ', random.randint(1, 7)) # random.randrange(1, 7+1)과 같은 의미임, 끝값 포함 O
print()

print("리스트에서 1개 값 꺼내오기")
season = ['봄', '여름', '가을', '겨울']
print('season : ', season)
print("random.choice(season) : ", random.choice(season))
print()

l = ['가', '나', '다', '라']
print('리스트 순서 섞기')
print('섞기 전 l = ', l)
random.shuffle(l)
print('random.shuffle(l)')
print("섞은 후 l = ", l)
print()

print("리스트에서 몇 개의 값을 중복하지 않고 3개 뽑기")
sample = ['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번', '9번']
print("샘플 대상 : ", sample)
print('random.sample(sample, 3) : ', random.sample(sample, 3))

