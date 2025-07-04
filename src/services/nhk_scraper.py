import requests
from bs4 import BeautifulSoup
import time

nhk_news_base_url = 'https://www3.nhk.or.jp'
nhk_news_url = f'{nhk_news_base_url}/news/'

#記事の概要を取得
def _get_summary(article_url):
    try:
        response = requests.get(article_url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        summary_soup = BeautifulSoup(response.text, 'html.parser')
        summary_tag = summary_soup.select_one('.content--detail-main p')
        
        return summary_tag.get_text(strip=True) if summary_tag else ''

    except requests.RequestException as e:
        print(f'概要の取得に失敗：{article_url}, error:{e}')
        return ''

def fetch_nhk_news():
    try:
        response = requests.get(nhk_news_url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        
        temp_articles = []

        #トップニュースのタイトル、urlを取得
        top_story = soup.select_one('h1.content--header-title a')
        if top_story:
            path = top_story.get('href','')
            if path and isinstance(path, str):
                url = f'{nhk_news_base_url}{path}' if path.startswith('/') else path

                temp_articles.append({
                    'title': top_story.get_text(strip=True),
                    'url': url,
                })

        #一覧記事のタイトル、urlを取得
        list_items = soup.select('ul.content--list dd > a')
        for item in list_items:
            path = item.get('href','')
            if path and isinstance(path, str):
                url = f'{nhk_news_base_url}{path}' if path.startswith('/') else path

                temp_articles.append({
                    'title':item.get_text(strip=True),
                    'url':url,
                })

        print(f'{len(temp_articles)}件の記事を取得しました')

        articles = []

        for article in temp_articles[:5]:
            summary = _get_summary(article['url'])

            articles.append({
                'title': article['title'],
                'summary': summary,
                'url': article['url']
            })

            #連続アクセスしないように1秒待機
            time.sleep(1)

        return articles
    
    except requests.RequestException as e:
        print(f'記事の取得に失敗: {nhk_news_url}, error:{e}')
        return []

if __name__ == '__main__':
    news_list = fetch_nhk_news()
    if news_list:
        for i, news in enumerate(news_list):
            print(f'[{i+1}]')
            print(f'タイトル: {news['title']}')
            print(f'概要: {news['summary']}')
            print(f'URL: {news['url']}')
            print('-'*50)
    else:
        print('記事の取得に失敗しました')
