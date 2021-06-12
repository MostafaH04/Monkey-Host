import time as tm
import json
import check

while True:
    with open('info.json') as infoFile:
        coming = json.load(infoFile)
    print(coming)

    time = ''
    timehrs = 0
    timemins = 0
    localTime = ''
    localTimeHrs = 0
    localTimeMins = 0
    try:
        for i in coming.keys():
            time = coming[i]
            timehrs = int(time[:time.index(":")])
            timemins = int(time[time.index(":")+1:])
            localTime = tm.asctime(tm.localtime()).split()[3]
            localTimeHrs = int(localTime[:localTime.index(":")]) - 12
            localTimeMins = int(localTime[localTime.index(":")+1:localTime.index(":")+3])
            
            if localTimeMins + 10 >= timemins:
                if timemins >= 9:
                    if localTimeHrs == timehrs:
                        if check.startSearch() == True:
                            coming.pop(i)
                            with open("info.json", "w+") as outfile: 
                                json.dump(coming, outfile)
                        check.vidOut(str(tm.time()))
                        
                else:
                    if localTimeHrs == timehrs - 1:
                        if check.startSearch() == True:
                            coming.pop(i)
                            with open("info.json", "w+") as outfile: 
                                json.dump(coming, outfile)
                        check.vidOut(str(tm.time()))
    except:
        print ("removed one")
