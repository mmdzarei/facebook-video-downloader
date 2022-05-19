# facebook-video-downloader-bot
This bot gets a facebook link and uploads it to the user
This is an old code, clean it up on your own

Add telegram token to **line 33** add trusted users to **line 38**, and add admin(bot owner's telegram user_id to **line 94**)

This was tested on python3.8

The code is messy, and telegram has been updated gazillion times, so please use it on your own risk.

HD downloader works right now but might stop working due to facebook xpath change. :D

## To use it in pythonanywhere.com
https://help.pythonanywhere.com/pages/selenium/

But **change** "browser = webdriver.Chrome(options=chrome_options)" to "browser = webdriver.Chrome(chrome_options=chrome_options)"


