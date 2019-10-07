# p.245
import array

f = open("data.bin", "rb")
data = f.read()
# print(data) # 16진수 출력
for item in data:
    print(item)
f.close()

