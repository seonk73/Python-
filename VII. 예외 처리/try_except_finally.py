f = open("file.txt", "w") # w는 write, r은 read

try:
    f.write("Hello World"+"\n")
    f.write("100")
except TypeError:
    print("타입 예외 발생(100은 쓸 수 X)")
finally:
    print("예외 여부와 상관없이 무조건 실행")
    f.close()