#.141

import hello_func
import greeting_func

def main():
  print("insa_func 모듈입니다.")
  print("__name__ : ", __name__) # __name__ : __main__
  hello_func.hello()
  greeting_func.greeting() # __name__ : greeting_func # 자기를 실행할 땐 __main__으로, 다른 곳에서 호출할 때는 누군가 호출한 것으로 받아들여서 import한 문장이 __main__을 대체.

main()
