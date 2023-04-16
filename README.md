# Poetic Rizz Bot

Poetic Rizz Bot is a bot that generates poetic rizz instagram reels.

## Installation
You need this following tools to be installed on your machine for  the bot to work :
- FFMPEG
- Chrome
- Chromedriver
- Selenium

## Usage

To use Poetic Rizz Bot:
- You can use an automated way to get poems :
    - Edit the getrizz.py file :
        - add the path to the chromedriver.exe
        - set the amount of poems you need
    - Run getrizz.py to generate the poems and put them in the rizzourses.txt file
    - Clean the rizzourses.txt file
- Or : just edit the rizzourses.txt file and add a poem for each line
- Edit the gensub.py file :
    - add the path of folder you are working on
- Run gensub.py to generate the SRT files needed for the video generation
- Run genrizz.py to generate the videos
