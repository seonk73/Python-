for x in range(3, 9, 2):
  print(x)
for ch in "Love":
  print(ch)
for item in ["힙합", "발라드"]:
  print(item + "을/를 즐겨듣는다.")
for item in (2560, 1440):
  print(item)
pl = {"C":1972, "Java":1995, "Python":1991}
for key in pl:
  print(key, ":", pl[key])
  # print(key + ":" + str( pl[key] )) # ,는 공백이 있고 +는 공백이 없음
for key, value in pl.items():
  print(key, ":", value)
for item in {"HTML5", "CSS3", "JavaScript"}: # 집합이므로 순서는 랜덤
  print(item + "을/를 할 수 있다.")

# 리스트 안의 리스트

table = [
  ["월", "화", "수"],
  [1, 2, 3]
]
for row in table:
    for col in row:
      print(col)
    print("------")


    
