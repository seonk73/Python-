dan = 2
for dan in range(2, 9+1): # 맨 앞에는 띄어쓰기 X -> IndentationError
  for i in range(1, 9+1):
    if i % 2 == 0:
      continue
    print(dan, " x ", i, " = ", dan*i)
  print("----------------") # Python은 띄어쓰기가 정말 중요함 -> 중괄호가 없기에
  

    