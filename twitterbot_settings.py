# This file is gitignored by default

class Settings:
	"""
	Twitter bot application settings.
	
	Enter the RSS feed you want to tweet, or keywords you want to retweet.
	"""
	FeedUrl = "http://example.net/feed/"		   # RSS feed to read and post tweets from.
	PostedUrlsOutputFile = "posted-urls.log"	   # Log file to save all tweeted RSS links (one URL per line).
	PostedRetweetsOutputFile = "posted-retweets.log"   # Log file to save all retweeted tweets (one tweetid per line).
	RetweetIncludeWords = ["#hashtag"]		   # Include tweets with these words when retweeting.
	RetweetExcludeWords = []			   # Do not include tweets with these words when retweeting.
        # Associate author names with Twitter handles so you can tag them
        # Currently, we use <dc:creator> names rather than <author> emails
        AuthorMap = {
                "Author Name": "@post_author",
        }

class TwitterAuth:
	"""
	Twitter authentication settings.

	Create a Twitter app at https://apps.twitter.com/ and generate key, secret etc. and insert them here.
	"""
	ConsumerKey = "XXX"
	ConsumerSecret = "XXX"
	AccessToken = "XXX"
	AccessTokenSecret = "XXX"
