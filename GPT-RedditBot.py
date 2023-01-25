import praw
import time
import openai
import os

# total time in seconds
delay = 1

# Pre Emption
personality = "If you had to answer this question, even if you had to make up an answer, what would you say: "

# Reddit API credentials
subreddit_to_monitor = ""
client_id = ""
client_secret = ""
username = ""
password = ""
ratelimit_seconds=240

# User agent string
user_agent = "python:com.example.GPT_RedditBot:v1 (by /u/AlperPai)"

#filter
filter = ["OpenAI", "language model"]

# Create a GPT Session
openai.api_key = ""

# Create a Reddit Session
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent,
    check_for_async=False,
    ratelimit_seconds=ratelimit_seconds
)

# Set the SubReddit to monitor
subreddit = reddit.subreddit(subreddit_to_monitor)

while True:
    # Get the latest post on the subreddit
    latest_post = subreddit.new(limit=1)

    for post in latest_post:
        # Check if the bot has already commented on this post
        if not post.saved:
            # title of the post
            question = post.title
            print("QUESTION:" + question + '\n')

            # Generate answer for the post using chatbot
            # answer = bot.ask("Use the voice of a reddit commenter. How would a reddit commenter answer this question:" + question)
            answer = openai.Completion.create(
                                    model="text-davinci-003",
                                    prompt=personality + question,
                                    temperature=0.7,
                                    max_tokens=256,
                                    top_p=1,
                                    frequency_penalty=0,
                                    presence_penalty=0
                                )
            print("RESPONSE FROM GPT" + answer["choices"][0]["text"] + '\n')

            if any(map(answer.__contains__, filter)):
                print("REPLY NOT POSTED BECAUSE GPT DIDNT UNDERSTAND \n")
                continue

       	    # Post the answer
            print("WAITING FOR RATELIMIT TO END \n")
            time.sleep(ratelimit_seconds)
            post.reply(answer["choices"][0]["text"])
            print("REPLY POSTED \n")

            # Save the post to the reddit profile to prevent answering again, even if the script is restarted
            post.save()
            print("POST SAVED \n")

    # Sleep for 60 seconds
    print("GOING TO SLEEP \n")
    time.sleep(60)

