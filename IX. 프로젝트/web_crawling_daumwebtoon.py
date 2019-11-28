# pip install beautifulsoup4
# pip install lxml
import json

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    # 다음 웹툰 > 취향저격 그녀 제목 가져오기
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data:
        j = json.loads(data.read()) # httpResponse -> json로 바꿔주기
    # print(j['data']['webtoon']['webtoonEpisodes'][3]['title'])
    cartoon_titles = j['data']['webtoon']['webtoonEpisodes'] # data.webtoon.webtoonEpisodes : 리스트로 가져옴
    for cartoon_title in cartoon_titles:
        title = cartoon_title['title']
        print(title)
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        print(thumbnail)
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/" + str(url)
        print(url)


    # html = "<html><head><meta charset='utf-8'></head><body>"
    # cartoon_titles = soup.find_all("td", attrs={"class":"title"}) # <td class="title">...</td>
    # for cartoon_title in cartoon_titles:
    #     title = cartoon_title.find("a").text # <a>text</a> & text를 하면 태그가 감싸져있는 제목만 가져올 수 있음
    #     link = cartoon_title.find("a").get("href") # <a href="">text</a> -> 태그의 속성값 가져오기
    #     link = "https://comic.naver.com" + link
    #     # print(title)
    #     # print(link)
    #     html += "<a href='{}'>{}</a>".format(link, title) # <a href='link'>title</a>
    # html += "</body></html>"
    # print(html)
    # outputSoup = BeautifulSoup(html, "lxml") # 내가 생성한 html 문자열을 soup 객체로 만들기
    # prettyHtml = str(outputSoup.prettify()) # 예쁘고 정돈된 형태로 html 코드 만들기
    # with open("연애혁명.html", "w", encoding="utf-8") as f:
    #     f.write(prettyHtml)