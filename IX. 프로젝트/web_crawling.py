# pip install beautifulsoup4
# pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    # 네이버 웹툰 > 연애혁명 제목 가져오기
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=570503")
    soup = BeautifulSoup(data, "lxml") # httpResponse -> HTML로 바꿔주기
    # print(soup)
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = soup.find_all("td", attrs={"class":"title"}) # <td class="title">...</td>
    for cartoon_title in cartoon_titles:
        title = cartoon_title.find("a").text # <a>text</a> & text를 하면 태그가 감싸져있는 제목만 가져올 수 있음
        link = cartoon_title.find("a").get("href") # <a href="">text</a> -> 태그의 속성값 가져오기
        link = "https://comic.naver.com" + link
        # print(title)
        # print(link)
        html += "<a href='{}'>{}</a>".format(link, title) # <a href='link'>title</a>
    html += "</body></html>"
    # print(html)
    outputSoup = BeautifulSoup(html, "lxml") # 내가 생성한 html 문자열을 soup 객체로 만들기
    prettyHtml = str(outputSoup.prettify()) # 예쁘고 정돈된 형태로 html 코드 만들기
    with open("연애혁명.html", "w", encoding="utf-8") as f:
        f.write(prettyHtml)