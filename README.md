# GPT-RedditBot
This bot uses GPT-3 to comment on recent reddit posts. This repo is a modified version of [PopDaddyGames ChatGPT bot](https://github.com/PopDaddyGames/ChatGPT-RedditBot)

# WARNING
YOU WILL PROBABLY GET [SHADOWBANNED](https://www.reddit.com/r/ShadowBan/comments/8a2gpk/an_unofficial_guide_on_how_to_avoid_being/) WHEN YOU USE THIS BOT SO BE AWARE. [I GOT SHADOWBANNED WHILE USING THIS.](https://www.reddit.com/r/ShadowBan/comments/10kuzx5/am_i/)

# Instalation

1. Have a OpenAI Account

2. Generate a Reddit [Client ID & Secret Key](https://www.reddit.com/prefs/apps)

3. Get your [OpenAI API Key](https://beta.openai.com/account/api-keys)

4. Configure

```
# Pre Emption
personality = "If you had to answer this question, even if you had to make up an answer, what would you say: "

# Reddit API credentials
subreddit_to_monitor = ""
client_id = ""
client_secret = ""
username = ""
password = ""
ratelimit_seconds=240

# Create a GPT Session
openai.api_key = ""

```
5. Install Dependencies

```
pip install openai time praw
```
and finally,

6. Run the bot
```
python GPT-RedditBot.py
```

## Prompts

# Code Helper
This prompt is for subreddits that are for communities that is related to coding
```
Pretend to be a reddit user on r/CodingHelp commenting on users posts (You wont be chatting with the user through a chatbox. Imagine that you are in a forum.). Try to help users in the subreddit. If they ask for code, give the code. As always, DO NOT SAY THAT YOU ARE AN AI IN ANY SHAPE OR FORM. ACT LIKE YOU ARE A HUMAN: 
```

# Question Answerer
This prompt is for subreddits like askreddit
```
Pretend to be a reddit user that isn't a robot. If you had to answer this question, even if you had to make up an answer, what would you say: 
```
