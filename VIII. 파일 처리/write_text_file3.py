fi = open("test.ama", "w", encoding="utf8")
fi.write("아이스아메리카노\t2800\t0\t2\t1\t1\n")
fi.write("오레오쉐이크\t3500\t1\t1\t3\t3\n")
fi.write("딸기코코넛\t3800\t1\t0\t3\t3\n")

fi.close()

fi = open("test.ama", "r", encoding="utf8")
sum = 0
while True:
    data = fi.readline()
    if not data:
        break
    l = data.split() # 쪼개서 담는거 / 화이트 스페이스(띄어쓰기, \t, \n 등)로 분리
    print(l[1] + "원")
    sum += int(l[1])
fi.close()
print("주문한 총 금액 : " + str(sum) + "원")
