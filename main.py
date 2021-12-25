#  Bryan Gamble 251025705
#  Twiter Sentiment Analysis

from sentiment_analysis import compute_tweets

tweets = input("Name of file containing tweets:")
keywords = input("Name of file containing keywords:")

output = compute_tweets(tweets,keywords)

if output == []:
    print(output)
else: 
    print("Eastern Region: Happiness score: %.3f," % (output[0][0]),output[0][1],"keyword tweets,",output[0][2],"tweets in total for this region")
    print("Central Region: Happiness score: %.3f," % output[1][0],output[1][1],"keyword tweets,",output[1][2],"tweets in total for this region")
    print("Mountain Region: Happiness score: %.3f," % output[2][0],output[2][1],"keyword tweets,",output[2][2],"tweets in total for this region")
    print("Pacific Region: Happiness score: %.3f," % output[3][0],output[3][1],"keyword tweets,",output[3][2],"tweets in total for this region")
