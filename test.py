from datetime import date
import datetime
"""
jz = datetime.datetime.now().strftime('%d %m %Y %H %M %S')
f = open("./cooldown/Flawless Desire#1525.txt", "w")
f.write(str(jz) + "\n")
f.close()
"""

DD = datetime.timedelta(seconds=10)



def quest():
    f = open("./cooldown/Flawless Desire#1525.txt", "r")
    cd = datetime.datetime.strptime(f.read().rstrip(),'%d %m %Y %H %M %S')
    f.close()
    print(cd)
    if datetime.datetime.today() - DD >= cd:
        print ("yes!")
    else:
        print("no :(")

quest()