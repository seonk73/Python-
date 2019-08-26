# 학번 -> 학과
majors = ["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
["뉴미디어소프트웨어과", "뉴미디어웹솔루션과", "뉴미디어디자인과"],
["인터렉티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]

# 학번 입력 
# start ---
studentNumber = input("학번 입력 : ")

# 학과 출력
grade = studentNumber[0:1]
grade =  int(grade)
classroom = studentNumber[1:2]
classroom = int(classroom)
print(majors[grade-1][classroom-1]//2)
# --- end

# grade와 class에 값을 넣어놓고, if에서 grade와 class를 사용해서 연산 가능
# if studentNumber[0:1] == "3" : # 문자열 -> " " 
#   if studentNumber[1:2] == "1" or studentNumber[1:2] == "2" :
#     print(majors3학년[classroom-1]//2) #그냥 /하면 소수로 나옴 -> //
# elif studentNumber[0:1] == "1" or studentNumber[0:1] == "2" :
#    print(majors12학년[classroom-1]//2)

   



