import Question
import sys

class Result:
    # 각 피부 타입에 맞는 관리 팁을 보여주기 위한 함수
    def print_result(self, q1):
        print("\n")
        print("-----------------------------------------------------------------------------------------------------")
        print("\n")
        if q1.skinType == "지성":
            print("관리 팁 ↓ ")
            print("\n▷▶  화장품 : 피지조절제가 함유된 지성 타입의 화장품 추천")
            print("\n▷▶  클렌징 : 클렌징 폼 or 워터 타입의 클렌징 제품 사용")
            print("\n--->  이중 클렌징 & 주 1, 2회 각질 제거 추천")
            print("\n▷▶  스킨케어 :  토너 - 로션 - 수분크림 순서로 사용")
            print("\n")
            print("-----------------------------------------------------------------------------------------------------")
        elif q1.skinType == "중성":
            print("관리 팁 ↓ ")
            print("\n▷▶  화장품 : 유수분이 적절하게 섞인 제품을 추천")
            print("\n▷▶  클렌징 : 어떤 제품과 어떤 방식이든 화장이 잘 지워지면 OK")
            print("\n▷▶  스킨케어 : 현재 피부의 유수분 밸런스가 좋은 상태")
            print("\n--->  중성은 이상적인 피부상태이지만, 꾸준한 관리가 필요함")
            print("\n")
            print("-----------------------------------------------------------------------------------------------------")
        elif q1.skinType == "건성":
            print("관리 팁 ↓ ")
            print("\n▷▶  화장품 : 영양과 보습 성분이 함유된 오일 or 에센스 추천")
            print("\n▷▶  클렌징 : 페이셜 클렌저 사용 추천 (오일 or 크림 타입)")
            print("\n▷▶  스킨케어 : 토너 - 보습 크림 - 페이스오일 순서로 사용")
            print("\n--->  건성은 피부가 약하므로 문지르는 것보다 부드럽게 두드려 흡수시키는 것을 추천")
            print("\n")
            print("-----------------------------------------------------------------------------------------------------")

    # 결과를 보여준 뒤, 결과를 저장할 것인지 선택하는 함수
    def end(self, q1):
        e = input("\n결과를 저장하시겠습니까? (Y : 결과 저장 / N : 프로그램 종료) : ")
        if e == "Y" or e == "y": # 결과를 저장한다고 입력(Y)하면, 파일에 피부 타입을 저장해놓기
             f = open("file.txt", "w", encoding="utf8")
             skin = q1.skinType
             f.write(str(skin))
             f.close
        else:
            sys.exit()  # 전체 프로그램에서 탈출