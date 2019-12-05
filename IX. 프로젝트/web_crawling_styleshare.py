# pip install beautifulsoup4
# pip install lxml
import json

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    # 스타일쉐어 > 스타일피드 가져오기 (못하겠다)
    with urlopen("https://www.styleshare.kr/isora95/136169930") as data:
        j = json.loads(data.read()) # httpResponse -> json로 바꿔주기
    # print(j['data']['webtoon']['webtoonEpisodes'][3]['title'])
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = j['data']['webtoon']['webtoonEpisodes'] # data.webtoon.webtoonEpisodes : 리스트로 가져옴
    for cartoon_title in cartoon_titles:
        title = cartoon_title['title']
        print(title)
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        print(thumbnail)
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/" + str(url)
        html += "<a href='{}'><img src='{}'/></a>".format(url, thumbnail, title)
    html += "</body></html>"

    outputSoup = BeautifulSoup(html, "lxml")  # 내가 생성한 html 문자열을 soup 객체로 만들기
    prettyHtml = str(outputSoup.prettify()) # 예쁘고 정돈된 형태로 html 코드 만들기
    with open("스타일피드.html", "w", encoding="utf-8") as f:
        f.write(prettyHtml)
