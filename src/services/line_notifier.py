import os
import requests

LINE_NOTIFY_TOKEN = os.environ.get('LINE_NOTIFY_TOKEN')
LINE_NOTIFY_API_URL = 'https://notify-api.line.me/api/notify'

def send_line_notification(message: str):
    if not LINE_NOTIFY_TOKEN:
        print('エラー：LINE_NOTIFY_TOKENが設定されていません')
        return False
        
    try:
        headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
        data = {'message': message}

        response = requests.post(LINE_NOTIFY_API_URL, headers=headers, data=data)
        response.raise_for_status()
        return True
   
    except requests.RequestException as e:
        print(f'LINE通知の送信に失敗しました: {e}')
        return False



