import time

def LINEnotify(msg):

    import requests
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    # msg = 'ETIC LAB - PClab'

    # payload = {'message': msg, 'stickerPackageId': 4, 'stickerId': 629} #2/39 3/198
    payload = {'message': msg}
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
    # files = {"imageFile": open("HOME.jpg", "rb")}
    r = requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)
    # r = requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers, files=files)
    print(r)
    return r

while 1:
    LINEnotify('MSG from Pycharm')
    time.sleep(10)

# https://devdocs.line.me/files/sticker_list.pdf