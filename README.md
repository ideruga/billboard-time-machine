# billboard-time-machine
Scraping billboard list for a random date and adding the songs to a Spotify playlist.
Based on [100 Days of Code - The Complete Python Pro Bootcamp for 2021](https://www.udemy.com/course/100-days-of-code), 
day 45.


## Description
This module scrapes the billboard website for a list of top 100 songs on a random date within past 20 years (max for 
billboard) and adds them to the Billboard Time Machine playlist on Spotify, flushing it preliminarily. 

## Architecture
This module can be used as an AWS lambda (or another serverless cloud solution) in conjunction with AWS Rules to 
reset the playlist every midnight. Google Home (Alexa, IFTTT, etc) can be used to start your playlist, e.g. at 7am 
on your preferred device e.g. Google Home.


## Deployment
1. Create a deployment folder with all .py files. 
2. Go into venv/Lib/site-packages and copy the following folders into the deployment folder:
* bs4
* certifi
* chardet
* dateutil
* idna
* requests
* soupsieve
* spotipy
* urllib3

3. Run the script and authenticate with spotify. When everything works, copy .cache file to the deployment folder.
4. Create a .zip file with the contents of the deployment folder and deploy it as a lambda.
5. Create a rule in AWS to launch the lambda at midnight (mind the timezone!).



## Improvements

1. Add scraped year to the playlist description.
2. Use GitHub automation to deploy the lambda and the rule.