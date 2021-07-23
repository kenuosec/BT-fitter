# coding=UTF-8

import requests


def get_response(url):
    try:
        response = requests.get(url, timeout=3)
        res = response.text
        print(url)
        return res
    except:
        return 'null response'


def ext_result(name, result):
    file = open(name + '.txt', "a+")
    file.write(result + '\r')
    file.close()


file = open("results.txt", "r", encoding='utf-8')

for line in file:
    wordlist = line[0:-1]
    targeturl = 'http://' + wordlist + ':8888'
    print('Testing', targeturl)
    text = get_response(targeturl)
    print(text)

    if 'null' in text:
        print('==========')
        print('Access Denied')
        print('==========')

    elif 'etc' in text:
        print('==========')
        print('BT linux sever')
        print('==========')
        ext_result('BTlinuxsever', wordlist)
    if 'limitip' in text:
        print('==========')
        print('BT linux sever')
        print('==========')
        ext_result('BTlinuxsever', wordlist)
    elif '扫一扫' in text or 'www.bt.cn' in text:
        print('==========')
        print('BT Panel')
        print('==========')
        ext_result('BTpanel', targeturl)
    elif '桌面面板图标' in text:
        print('==========')
        print('BT windows sever')
        print('==========')
        ext_result('BTwindowssever', wordlist)
    elif '401 Unauthorized: Password required' in text:
        print('==========')
        print('Basic Auth')
        print('==========')
        ext_result('BasicAuth', targeturl)
    else:
        continue

