# Reddit TikTok Video Bot 

RedditTikTokBot automates the creation of the viral TikTok Reddit comment-read video format by compiling gameplay and sourcing interesting threads from various subreddits to allow users to generate unlimited content for spaces such as TikTok, Youtube shorts, and Instagram Reels!  

Please include a link to this [GitHub Repo](https://github.com/alexandertomsovic/RedditTikTokBot) in the comments section of your videos. Enjoy!

Created by [Alexander Tomsovic](https://linktr.ee/alextomsovic)

<a target="_blank" href="https://alextomsovic1.wixsite.com/my-site">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/84757117/185300584-bf5c08aa-15a5-442c-a580-87c3a701c5b7.png">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/84757117/185300584-bf5c08aa-15a5-442c-a580-87c3a701c5b7.png">
  <img src="" width="350">
</picture>
</a>

## Utility 

TikTok trends have changed with the newest trend being emotional, creepy, or enchanting reddit threads read aloud with Minecraft gameplay played in the background. 
Having seen hundreds of vidoes in this format go viral, I decided to build a program to automate this process. 

## Disclaimer

**At this current time**, this program will not upload final output videos to TikTok. It will store them in the *results* folder where you can upload them manually. 
We are working to implement an feature that will allow instant autonomous uploads! Check the repository page for updates! () **UPDATE**

## Requirements

- Python 3.8+
- Playwright (should be installed with requirements in the first installation leg)
- [SoX](https://sourceforge.net/projects/sox/files/sox/)

## Initial Installation 

1. Clone this repository via [GitHub](https://github.com/alexandertomsovic/RedditTikTokBot)

2. 2A **Automatic Install**: Run `python main.py` and type "yes" to initiate automatic setup. 
   If this step fails, try manually installing.

   2B **Manual Install**: Rename the `.env.template` file to `.env` and enter the correct values into each field. CASE SENSITIVE! Reddit Keys for the *CLIENT ID* and *Secret Key* can be found here: [the Reddit Apps page.] (https://www.reddit.com/prefs/apps) 
   

## Getting Reddit Keys:

-  Click "Create App" 
-  Choose the "Script" option
-  Copy your *CLIENT ID* and *Secret Key* into the `.env` file
-  Enter the remaining items into the appropriate fields. 

## Primary Installation

1. Install [SoX](https://sourceforge.net/projects/sox/files/sox/)
   
2. Run `pip install -r requirements.txt` into your Python Terminal.

3. Run `playwright install` and `playwright install-deps`. (Add python -m to the front of the command if this step fails)

4. Run `python main.py` if you chose to manually install this repository, otherwise this will automatically run. 

5. Happy Automating!

If  you get an error installing or running the bot:

-  Rerun the command with a "3" after the name (python3 or pip3)
-  Reinstall the repository from [GitHub](https://github.com/alexandertomsovic/RedditTikTokBot)
- Create a Repository pull request via GitHub

## Video

https://user-images.githubusercontent.com/66544866/173453972-6526e4e6-c6ef-41c5-ab40-5d275e724e7c.mp4

## Contributions / Future Improvements 

RedditTikTokBot works perfectly in its current version, but I believe there is a lot to be desired. Here are a list of items that should be implemented in the near future in order to maximize this program's utility.

- [ ] Automatic uploads to social media accounts.
- [ ] Writing a thourough documentation and impementing a CLI.
- [ ] Bypassing *CLIENT ID* and *Secret Key* requirements. 
- [x] Allowing custom reddit threads. 
- [x] Allowing users to choose a background that is picked instead of the Minecraft one.
- [x] Allowing users to choose between any subreddit.
- [x] Allowing users to change voice.
- [x] Checks if a video has already been created
- [x] Light and Dark modes
- [x] NSFW post filter

Please read the [contributing guidelines](CONTRIBUTING.md) for more information!


------------------------------------------------------------------------------------
RedditTikTokBot, an opensource project by A.R.T. LLC.

Owned and operated by *Alexander Tomsovic*

[LinkTree](https://linktr.ee/alextomsovic) | [Replit](https://replit.com/@alextomsovic) | [inStock](https://instockapp.org) | [LexBot](https://lexbot.org)



