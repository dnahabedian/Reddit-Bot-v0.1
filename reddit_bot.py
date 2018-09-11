#all of the imported packages
import praw
import config
import time
import os


#define what the method of bot_login() does (gets the data from the config file using Reddit user data)
#creates a new "Reddit instance" named r
def bot_login():
	print ("logging in...")
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "dnahabedianRedditBot's bald fraud status comment bot v0.1")
	print ("Logged in!")

	return r






#method of what the bot will do once it is run
def run_bot(r):
	print ("Searching through 10 comments...")


	for comment in r.subreddit('test').comments(limit = 10):

		if "bald fraud" in comment.body and comment.id not in comments_replied_to_already and comment.author != r.user.me():
			print ("Found something! in" + comment.id)
			comment.reply("FRAUD STATUS: BALD")
			print ("Replied to comment with a status report!" + comment.id)

			comments_replied_to_already.append(comment.id)

			with open ("comments_replied_to_already.txt", "a") as commentFile: #"a" means append
				 f.write(comment.id + "\n")

	#rests the bot for certain allocated amount of time in order to not spam Reddit/users
	print ("Sleeping now for 3 minutes...")
	#Sleep for 180 seconds...
	time.sleep(180)		







#method to record, save, and add comments to a list in order to have a record so bot doesn't reply to itself
#or other comments that it has already commented in before
def get_saved_comments():

	if not os.path.isfile("comments_replied_to_already.txt"): #looking for txt file, if not there makes new list
		comments_replied_to_already = []
	else:	
		with open("comments_replied_to_already.txt", "r") as commentFile: #"r" means read
			comments_replied_to_already = commentFile.read()
			comments_replied_to_already - comments_replied_to_already.split("\n")
			comments_replied_to_already = filter(None, comments_replied_to_already) #filter removes the empty character in the list

	return comments_replied_to_already








#actually running the bot calling bot_login, and get_saved_comments
#While loop runs the bot indefinitely so the bot can continue to search comments
r = bot_login()
comments_replied_to_already = get_saved_comments()

while True:
	run_bot(r)