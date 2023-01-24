# GPT-RedditBot
This bot uses GPT-3 to comment on recent reddit posts.

# WARNING
YOU WILL PROBABLY GET SHADOWBANNED WHEN YOU USE THIS BOT SO BE AWARE. I GOT SHADOWBANNED WHILE USING THIS.

# Instalation

1. Have a OpenAI Account

2. Generate a Reddit [Client ID & Secret Key](https://www.reddit.com/prefs/apps)

3. Get your [OpenAI API Key](https://beta.openai.com/account/api-keys)

4. Configure

```
# Reddit API credentials
subreddit_to_monitor = ""
client_id = ""
client_secret = ""
username = ""
password = ""
ratelimit_seconds=240
```
5. Install Dependencies

```
pip install openai time praw
```
and finally,

6. Running the bot
```
python GPT-RedditBot.py
```
