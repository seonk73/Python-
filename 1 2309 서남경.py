# 학번을 입력받고,
# 학년 학과 반 번호를 출력

majors = [["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
["인터렉티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]]

studentNumber = input("학번 입력 : ")

grade = studentNumber[0]
grade = int(grade)
classroom = studentNumber[1]
classroom = int(classroom)
number = studentNumber[2:]
number = int(number)
major = majors[(grade)-1][((classroom)-1)//2]
print(grade,"학년", major, classroom,"반", number,"번 입니다.")