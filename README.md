<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/OugiFormula/Jarrot-bot/">
    <img src="https://i.imgur.com/XpwqV00.png" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">JarrotBot</h3>

  <p align="center">
    Best jarrot bot on the internet!
    <br />
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Instructions](#instructions)



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="https://i.imgur.com/sCthP6y.png" alt="jarrot" width="150" height="150">

Jarrot, oh the mighty jarrot you never ever had a bot related to you. therefore I represent to you the jarrot bot.

You can:
* Grab images from r/jarrot
* 8-ball themed jarrot. yes mighty jarrot


### Built With
* [Python](https://python.org)




<!-- GETTING STARTED -->
## Instructions

Step 1 | you need to choose prefix for the bot you can find it in line 21.
client = commands.Bot(command_prefix="Your Prefix here")

Step 2 | setup your reddit connection

For this part you need:
* Reddit account
* Reddit API ID and secret code

if you don't have reddit account create one on https://www.reddit.com/register/

first let's add our username and password on line 11

reddit = praw.Reddit(
    client_id=REDDIT_APP_ID,
    client_secret=REDDIT_APP_SECRET,
    password="Your reddit password here",
    user_agent="anynameyouwanthere",
    username="your reddit username here",
)

That was the easy part now we need to create a new reddit application on the following link
https://ssl.reddit.com/prefs/apps/

Scroll down until you see "Create another app..."
Choose script option and give it a name.
Set redirect url to "https://localhost"

you will see two api keys:
* One will be under "personal use script" (REDDIT_APP_ID)
* One will be on the right side of "secret" (REDDIT_APP_SECRET)

On lines 8 and 9 we will insert the api keys

REDDIT_APP_ID="GET THIS FROM REDDIT"
REDDIT_APP_SECRET="GET THIS FROM REDDIT FFS"

The user_agent can be anything you want! make sure you don't use bot in it.

Step 3 | getting bot token and inviting to the discord server.
Make sure your'e logged on to the Discord website.
Navigate to the application page https://discord.com/developers/applications
Click on the "new application" button
Give the application a name and click "Create". (I recommend calling it jarrot)
Create a Bot User by navigating to the “Bot” tab and clicking “Add Bot”.

* Click “Yes, do it!” to continue.

Make sure that Public Bot is ticked if you want others to invite your bot.

* You should also make sure that Require OAuth2 Code Grant is unchecked unless you are developing a service that needs it. If you’re unsure, then leave it unchecked.

Copy the token using the "Copy" button
Paste it inside line 6
DISCORD_BOT_TOKEN="INSERT BOT TOKEN HERE"

In-order to invite the bot into your server you need to go back into the bot page.
Go to the "OAuth2" tab
Tick the "bot" checkbox under "scopes"
the bot only need couple permissions and they are to send messages, view channels.
To give the bot those permissions go to the "Bot Permissions" under the "Scopes"
Now the resulting URL can be used to add your bot to a server. Copy and paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.

That's it! your ready to run the bot and test all of the commands!

##Command List

* (prefix)mightyjarrot (question)
The following command will send a random image of jarrot with yes/no answers.

* (prefix)jarrot
The following command will send random image of jarrot taken from r/jarrot.

##Have fun playing with the bot!
