f = open("file.txt", "a") # a는 append의 약자 / 덮어쓰는건 w, 붙히는건 a
f.write("Hello")
f.write("\n")
f.write("world")

f.close()