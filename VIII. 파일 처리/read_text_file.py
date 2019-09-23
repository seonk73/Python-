f = open("file.txt", "r", encoding="utf8") # r은 read의 약자

text = f.read() # 읽어온 것을 변수에 넣어야함
print(text)

f.close()

# 한 줄 씩 읽어오기

f = open("file.txt", "r", encoding="utf8") # r은 read의 약자

text0 = f.readline() # 읽어온 것을 변수에 넣어야함 / \n까지 읽기
print(text0) # \n
text1 = f.readline() # 읽어온 것을 변수에 넣어야함
print(text1)

f.close()
