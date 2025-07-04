from services.nhk_scraper import fetch_nhk_news
from services.line_notifier import send_line_notification
from models.article import Article

def main():
    news_data_list = fetch_nhk_news()
    if not news_data_list:
        print('通知するニュースがありませんでした')
        return
    
    articles = [Article(**data) for data in news_data_list]

    if articles:
        target_articles = articles[0]
        message = target_articles.create_message()
        send_line_notification(message)
    
if __name__ == '__main__':
    import os
    os.environ['LINE_CHANNEL_ACCESS_TOKEN'] = 'MPsKmoHcO6JFmJEMkNuFu14q2UmYvoblDdgdjveWbMKw46RK4T6GCJ4HMdaZVZVVX7GO8qYtrbyRyHFjBXR++w15Px7SSMu2YCfm2UrXZ1XPnA1LrciMSTzac5XQ/oV3xzenryDxzo5zdPEaZcvlKAdB04t89/1O/w1cDnyilFU='
    os.environ['YOUR_USER_ID'] = 'U4b909b5b0c4d98e350e86e99ae753cbe'

    main()
