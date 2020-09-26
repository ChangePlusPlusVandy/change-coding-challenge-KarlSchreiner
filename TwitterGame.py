#
#  @brief a game which accepts two twitter usernames, compiles their most recent tweets, and prompts the player
#  to guess which of the two twitter users made that tweet. Created for the Change++ coding challenge.
#  @author Karl Schreiner karl.f.schreiner@vanderbilt.edu
#  last changed 9/25/2020
import tweepy
import random


class TwitterGame:
    # set up twitter api
    consumer_key = 'EfwIoQSVMtsaAQ2LtlVfPjHc5'
    consumer_secret = 'xshPa2wt6FqEJPKA9kFBXjMDfBMGFfafd0tSYDV4Ch1P9fcagZ'
    access_token = '1231958236447825920-OceXJuXlh5gzO5IToVK3DKwLV9jgje'
    access_secret = '12Sg3cr9dJDNEQQH1fIJ4dZP5AAD2ncKfCpjmZ3lAH0ot'
    authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authentication.set_access_token(access_token, access_secret)
    api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    tweetArray1 = []
    tweetArray2 = []
    name1 = ""
    name2 = ""
    numGuesses = 0
    numRight = 0

    # Class Constructor
    # @brief creates a Twitter Game object initializing tweetArray1and2 to tweets made by username1and2.
    # Defaults to kanyewest and elonmusk.
    # @param username1 valid twitter username of an account -- defualts to kanyewest
    # @param username2 valid twitter username of an account -- defaults to elonmusk
    # @param count is the number of tweets that should be searched. Twitter limits the rate of access and as a result
    # this can take a while. It is recommended to keep count around 150.
    def __init__(self, username1="kanyewest", username2="elonmusk", count=150):
        self.name1 = username1
        self.name2 = username2
        self.GetTweets(username1, self.tweetArray1, count)
        self.GetTweets(username2, self.tweetArray2, count)

    # GetTweets
    # @brief populates an array with tweets. Tweets that are retweets or contain links will be omitted.
    # @param name the username of a twitter user
    # @array an array to be filled with tweets
    # @count the number of tweets to process. recommended to keep around 150 as this can take a while.
    def GetTweets(self, name, array, count):
        maxTweets = count
        print("downloading the tweets of " + name + " this might take a minute...")
        maxId = -1
        tweetCount = 0
        while tweetCount < maxTweets:
            if (maxId <= 0):
                newTweets = self.api.user_timeline(screen_name=name, result_type="recent", tweet_mode="extended")
            else:
                newTweets = self.api.user_timeline(screen_name=name, max_id=str(maxId - 1), result_type="recent",
                                                   tweet_mode="extended")

            if not newTweets:
                break

            for tweet in newTweets:
                if tweet.full_text.find("@") == -1 and tweet.full_text.find("https") == -1 and tweet.full_text.find(
                        'RT') == -1:
                    array.append(tweet.full_text)

            tweetCount += len(newTweets)
            maxId = newTweets[-1].id

    # OneRound
    # @brief Simulates one round of the game, prompting the user to guess which person made a tweet. Tracks results.
    # Will throw an error if tweetArray1 or tweetArray2 are empty
    def OneRound(self):
        print("guess whose tweet this is (" + self.name1 + "/" + self.name2 + ")")
        if random.randint(0, 1) == 0:
            who = self.name1
            print(self.tweetArray1[random.randint(0, len(self.tweetArray1) - 1)])
        else:
            who = self.name2
            print(self.tweetArray2[random.randint(0, len(self.tweetArray2) - 1)])

        userInput = input()
        while userInput != self.name1 and userInput != self.name2:
            print("you must guess " + self.name1 + " or " + self.name2 + ".")
            userInput = input()
        self.numGuesses += 1
        if userInput == who:
            self.numRight += 1
            print("Correct!")
        else:
            print("Wrong!")

    #  PrintResults
    #  @brief prints the player's total attempts and total correct guesses.
    def PrintResults(self):
        if self.numGuesses > 1 and self.numRight > 1:
            print("You guessed " + str(self.numGuesses) + " times and were right " + str(self.numRight) + " times!")
        elif self.numGuesses == 1 and self.numRight == 1:
            print("You guessed " + str(self.numGuesses) + " time and were right " + str(self.numRight) + " time!")
        else:
            print("You guessed " + str(self.numGuesses) + " time and were right " + str(self.numRight) + " times!")
