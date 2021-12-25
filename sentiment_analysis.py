def compute_tweets(tweets,keywords):
    try:
        with open(keywords,"r",encoding="utf-8") as keywords: #  Opens keyword file
            keyDic,keyList = {},[]
            for line in keywords:
                temp = line.replace(","," ")
                key,value = temp.split()
                keyList.append(key) # List of keywords
                keyDic[key] = value # Makes dictionary of keywords and their values
    except FileNotFoundError:
        return []

    try:
        with open(tweets,"r",encoding="utf-8") as tweets:
            test = []
            ptotals,mtotals,ctotals,etotals = 0,0,0,0
            pcount,mcount,ccount,ecount = 0,0,0,0
            ptweets,mtweets,ctweets,etweets = 0,0,0,0
            ekeycount,ckeycount,mkeycount,pkeycount = 0,0,0,0
            for line in tweets:
                r = 0
                newList = []
                lineSplit = line.split()
                for word in lineSplit:
                    x = (word.strip("!#$%&'()*+,./:;<=>?@[\]^_`{|}~")).lower() # Remove puncuation 
                    newList.append(x)
                lat, long = (newList[0]).strip("][,"), (newList[1]).strip("][")
                lat,long = float(lat),float(long) 
                if 49.189787 > lat > 24.660845 and -115.236428 >= long > -125.242264: # Determine which timezone
                    ptweets += 1
                    for word in newList:
                        if word in keyList:
                            r = 1
                        if word in keyList:
                            ptotals += int(keyDic[word])
                            pkeycount += 1
                            test.append(word)
                    pcount += r
                elif 49.189787 > lat > 24.660845 and -101.998892 >= long > -115.236428:
                    mtweets += 1
                    for word in newList:
                        if word in keyList:
                            r = 1
                        if word in keyList:
                            mtotals += int(keyDic[word])
                            mkeycount += 1
                            test.append(word)
                    mcount += r
                elif 49.189787 > lat > 24.660845 and -87.518395 >= long > -101.998892:
                    ctweets += 1
                    for word in newList:
                        if word in keyList:
                            r = 1
                        if word in keyList:
                            ctotals += int(keyDic[word])
                            ckeycount += 1
                            test.append(word)
                    ccount += r
                elif 49.189787 > lat > 24.660845 and -67.444574 >= long > -87.518395:
                    etweets += 1
                    for word in newList:
                        if word in keyList:
                            r = 1
                        if word in keyList:
                            etotals += int(keyDic[word])
                            ekeycount += 1
                            test.append(word)
                    ecount += r
                            
        if ekeycount > 0:
            eaverage = etotals/ekeycount
        else:
            eaverage = 0
        if ckeycount > 0:
            caverage = ctotals/ckeycount
        else:
            caverage = 0
        if mkeycount > 0:
            maverage = mtotals/mkeycount
        else:
            maverage = 0
        if pkeycount > 0:
            paverage = ptotals/pkeycount
        else:
            paverage = 0
        output = [(eaverage,ecount,etweets),(caverage,ccount,ctweets),(maverage,mcount,mtweets),(paverage,pcount,ptweets)]
        return(output)

    except FileNotFoundError:
        return []
                