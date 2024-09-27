from bs4 import BeautifulSoup
import  requests


url = "https://news.ycombinator.com/"

response = requests.get(url=url)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
articles_scores = soup.find_all(name="span", class_="score")

articles_text = []
articles_links = []
articles_score = []

# print(len(articles))
# for i in range(0, len(articles)):
#
#     articles_score.append(articles_scores[i].getText())
#     print(f"{i,articles_scores[i].getText()}")


for i in range(0, len(articles)):
    articles_text.append(articles[i].getText())
    articles_links.append(articles[i].find("a")["href"])
    try:
        articles_score.append(int(articles_scores[i].getText().split()[0]))
    except:
        pass


for i in range(1, len(articles)):
    print(f"{i}.{articles_text[i]}\nLink:{articles_links[i]}")
    try:
        print(f"Score: {articles_score[i]}")
    except:
        pass


max_num = max(articles_score)
print(max_num)
print(articles_score.index(max_num))
print(articles_text[22], articles_score[22], articles_links[22])

# with open("website.html", encoding="utf-8") as site:
#     contents = site.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title.string)
#
# # print(soup.p)
# all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
# #   print(tag.getText())
#     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# #
# # para = soup.find(name="h3", class_="heading")
# # print(para)
# #
#
# company_url = soup.select_one(selector="p a")
# print(company_url)