import json
import random
import string
import random
import json
from time import sleep
import requests
import os.path, subprocess
import os


def random_string(letters=string.ascii_uppercase, length=8):
    return ''.join(random.choices(letters, k=length))





while True:
    try:
        b = requests.get("https://forshodoxi.click").text
        print(f"{b}")
        file = open('mytest.html', 'w+')
        #str1 = 'Hello World. Keep Smiling!'
        file.write(b)
        file.seek(0, os.SEEK_SET)
        print(file.read())
        file.close()
        os.system('git add .')
        os.system('git commit -am.')
        os.system('git push -u -f origin --all')
        sleep(15)
    except:
        traceback.print_exc()
        sleep(1)

