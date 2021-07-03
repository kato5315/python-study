from selenium import webdriver
import pandas as pd
from time import sleep

browser = webdriver.Chrome()
browser.get('https://zenn.dev/search/')

elem = browser.find_element_by_class_name('TopicCardList_container__2Um6e')
elems_tags = elem.find_elements_by_tag_name('a')

keys = []
for tag in elems_tags:
    # TODO 普通にaタグのURL取得すればいい気がしたw
    keys.append(tag.text.lower)

df = pd.DataFrame()

title_values = []
href_values = []

for key in ["python", "typescript"]:
    url = "https://zenn.dev/topics/" + key
    browser.get(url)
    elem = browser.find_element_by_class_name(
        "ArticleList_listContainer__2I5Jw")
    articles = browser.find_element_by_tag_name("article")

    for article in articles:
        a = article.find_element_by_tag_name("div > a")
        print(a)
    sleep(2)

df["title"] = title_values

browser.quit()
