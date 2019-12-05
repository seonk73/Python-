# 복지로 > 복지서비스 > 한 눈에 보는 복지 정보 > 아동, 청소년 > 100개씩 보기

from bs4 import  BeautifulSoup
import requests

if __name__ == '__main__':
    url = "http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data = {"searchIntClId":"03", "pageUnit":"100"}
    with requests.post(url, data) as reponse:
        soup = BeautifulSoup(reponse.text, "lxml")
    # print(soup)
    titles = soup.select("dt.tit > a")  # <dt class = "title"><a></a></dt>
    for title in titles:
        print(title.text)
