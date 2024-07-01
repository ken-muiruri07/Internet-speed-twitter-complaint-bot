from twitter_bot import InternetSpeedTwitterBot
PROMISED_DOWN = 100
PROMISED_UP = 110

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_provider()


