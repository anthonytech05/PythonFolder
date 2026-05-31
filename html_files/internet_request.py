
import requests

URL = 'https://www.youtube.com/watch?v=EerdGm-ehJQ'


def requestFacebookPage():
    try :
        response = requests.get(url=URL)
        code = response.status_code
        is_ok = response.ok
        # response.json()
        html_text = response.text
        print(html_text)
        return html_text
    except Exception as e :
        print(f'Error occurred : {e}')
        return None


data = requestFacebookPage()

if data :
    with open("C:/Users/CHIDI/OneDrive/Desktop/Pythonfolder/html_files/fbk.html",'w') as fp :
        fp.write(str(data))
        fp.close()
        print('Successfully phisphed out facebook page!')