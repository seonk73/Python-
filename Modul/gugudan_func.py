# p.142

def gugudan_func(n):
  print(n, "단을 출력합니다.")
  for i in range(1, 9+1):
    print(n, "x", i, "=", n * i)

if __name__ == '__main__': 
  # 테스트코드할 때 매우 중요하다. 공부하여라. main을 해주면 다른 파일에서 실행되지 않고 다른 파일의 내용만 실행됨.
  # 자기 모듈 실행하면 실행되고, 다른데서 import하면 실행 안되게 해줌. (아마 서술형...?)
  gugudan_func(3)