import os
# data = os.listdir(".") # .은 현재 디렉토리, ..은 상위 디렉토리를 가리킴
data = os.listdir("c:\\")# 절대주소, 나의 위치와 관계가 없음 / "\\" or "\" or "/" 모두 상관없음
print(data)

for d in data:
    print(d)
    print("is directory?: " + str(os.path.isdir(d)))
    print("is file?: " + str(os.path.isfile(d)))