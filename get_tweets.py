import tweepy
import json

#Twitter API creds
#insert your details here
#consumer_key=
#consumer_secret=
#access_token=
#access_secret=

def get_all_tweets(screen_names):
    '''
    Get all the tweets (as many as twitter allows) for a list of SNs
    '''
    file = open('tweets.txt','w')
    
    for user in screen_names:
        print ('Getting the tweets of %s.' %user)
        #Authorise twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)

        #Initialise list for tweets to be stored
        alltweets = []

        #make request for most recent tweets and save them
        new_tweets = api.user_timeline(screen_name = user,
                                       count = 200)

        alltweets.extend(new_tweets)

        #ID of oldest tweet (minus one)
        oldest = alltweets[-1].id - 1

        #Grab as many tweets as you can
        while len(new_tweets)>0:

            new_tweets = api.user_timeline(screen_name = user,                                       count = 200,
                                       max_id = oldest)
            alltweets.extend(new_tweets)
                                           
            oldest = alltweets[-1].id - 1
                                           
            print('...%s tweets downloaded'%(len(alltweets)))

        #write the tweets to the text file
        
        
        print('Writing tweets to txt file. This may take some time. Please wait')

        for tweet in alltweets:
            file.write(',::,'.join([tweet.text,tweet.user.name]))
            file.write('\n')

        print('Done')
    file.close()

#How do I compare with presidents and presidential candidates
People_of_interest = ['@jamesblood',
                      '@realDonaldTrump',
                      '@SenSanders',
                      '@HillaryClinton',
                      '@BarackObama']

get_all_tweets(People_of_interest)

