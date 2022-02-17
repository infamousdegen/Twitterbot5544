import tweepy
import logging
import time
import random
from datetime import datetime, timedelta
import requests
from discord_webhook import DiscordWebhook

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()


def check_for_followers(api,recent_following_user1,user_1,recent_following_user2,user_2,recent_following_user3,user_3,recent_following_user4,user_4,recent_following_user5,user_5,recent_following_user6,user_6,recent_following_user7,user_7,recent_following_user8,user_8,recent_following_user9,user_9,recent_following_user10,user_10,recent_following_user11,user_11,recent_following_user12,user_12,recent_following_user13,user_13,recent_following_user14,user_14):

    while True:


        time.sleep(23)


        time.sleep(180)

        #user 1
        for user in tweepy.Cursor(api.friends, screen_name=user_1).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_1)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user1):
                recent_following_user1.append(latest_following)
                print(latest_following + " is followed by " + user_1)
                message=user_1+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)


        time.sleep(180)

        
        for user in tweepy.Cursor(api.friends, screen_name=user_2).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_2)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user2):
                recent_following_user2.append(latest_following)
                message=user_2+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)


        time.sleep(180)


        for user in tweepy.Cursor(api.friends, screen_name=user_3).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_3)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user3):
                recent_following_user3.append(latest_following)
                message=user_3+" just followed " + " https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)                
                requests.get(base_url2)
                time.sleep(5)


        time.sleep(180)

        for user in tweepy.Cursor(api.friends, screen_name=user_4).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_4)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user4):
                recent_following_user4.append(latest_following)
                message=user_4+" just followed " +"https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)


        time.sleep(180)


        for user in tweepy.Cursor(api.friends, screen_name=user_5).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_5)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user5):
                recent_following_user5.append(latest_following)
                message=user_5+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)


        time.sleep(180)

        
        for user in tweepy.Cursor(api.friends, screen_name=user_6).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_6)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user6):
                recent_following_user6.append(latest_following)
                message=user_6+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)



        time.sleep(180)

        for user in tweepy.Cursor(api.friends, screen_name=user_7).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_7)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user7):
                recent_following_user7.append(latest_following)
                message=user_7+" just followed " +"https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)


        time.sleep(180)

        for user in tweepy.Cursor(api.friends, screen_name=user_8).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_8)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user8):
                recent_following_user8.append(latest_following)
                message=user_8+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)



        time.sleep(180)


        for user in tweepy.Cursor(api.friends, screen_name=user_9).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_9)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user9):
                recent_following_user9.append(latest_following)
                message=user_9+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)


        time.sleep(180)
        #first 9


        for user in tweepy.Cursor(api.friends, screen_name=user_10).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_10)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user10):
                recent_following_user10.append(latest_following)
                message=user_10+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)
        time.sleep(180)


        for user in tweepy.Cursor(api.friends, screen_name=user_11).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_11)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user11):
                recent_following_user11.append(latest_following)
                message=user_11+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)
        time.sleep(180)

        
        for user in tweepy.Cursor(api.friends, screen_name=user_12).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_12)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user12):
                recent_following_user12.append(latest_following)
                message=user_12+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)
        time.sleep(180)
        
        for user in tweepy.Cursor(api.friends, screen_name=user_13).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_13)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user13):
                recent_following_user13.append(latest_following)
                message=user_13+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)
        time.sleep(180)
        
        
        for user in tweepy.Cursor(api.friends, screen_name=user_14).items(5):
            time.sleep(10)
            print("checking for new followings of "+user_14)
            latest_following = str(user.screen_name)
            if (latest_following not in recent_following_user14):
                recent_following_user14.append(latest_following)
                message=user_14+" just followed " + "https://twitter.com/"+latest_following
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/937756263184466001/tXdqn3HAgvWOD9ewRBv3AbOXia1ORhWZ86qrXjZHvJb5QXra8WnAa4V4ol-gL1I3ihIo",content=message)
                response = webhook.execute()
                base_url='https://api.telegram.org/bot5230523338:AAG_rRN7sCWq29CulfA-6zfYnE2C-Ej-UDk/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url)
                base_url2='https://api.telegram.org/bot5132351109:AAHolO_uuOj3uSq4e-W_77erZfTcSCdcrwo/sendMessage?chat_id=-1001180497796&text={}'.format(message)
                requests.get(base_url2)
                time.sleep(5)
        time.sleep(180)




        
        
    
        ran=[10,15,21,17,19,16,35,7,9]
        choice=random.choice(ran)
        time.sleep(choice*60)
            
    

#initial adding of followers to the array

recent_following_user1=[]
user_1="3azima85"
for user in tweepy.Cursor(api.friends, screen_name=user_1).items(10):
    new_follower=str(user.screen_name)
    recent_following_user1.append(new_follower)


time.sleep(40)

recent_following_user2=[]
user_2="@Cryptik1E"
for user in tweepy.Cursor(api.friends, screen_name=user_2).items(10):
    new_follower=str(user.screen_name)
    recent_following_user2.append(new_follower)

time.sleep(40)

recent_following_user3=[]
user_3="Crypt00_Pepe"
for user in tweepy.Cursor(api.friends, screen_name=user_3).items(10):
    new_follower=str(user.screen_name)
    recent_following_user3.append(new_follower)

time.sleep(40)

recent_following_user4=[]
user_4="0xDaes"
for user in tweepy.Cursor(api.friends, screen_name=user_4).items(10):
    new_follower=str(user.screen_name)
    recent_following_user4.append(new_follower)

time.sleep(40)

recent_following_user5=[]
user_5="duke_rick1"
for user in tweepy.Cursor(api.friends, screen_name=user_5).items(10):
    new_follower=str(user.screen_name)
    recent_following_user5.append(new_follower)


time.sleep(40)

recent_following_user6=[]
user_6="gabrielhaines"
for user in tweepy.Cursor(api.friends, screen_name=user_6).items(10):
    new_follower=str(user.screen_name)
    recent_following_user6.append(new_follower)


time.sleep(40)

recent_following_user7=[]
user_7="defikhalil"
for user in tweepy.Cursor(api.friends, screen_name=user_7).items(10):
    new_follower=str(user.screen_name)
    recent_following_user7.append(new_follower)


time.sleep(40)

recent_following_user8=[]
user_8="cryptodetweiler"
for user in tweepy.Cursor(api.friends, screen_name=user_8).items(10):
    new_follower=str(user.screen_name)
    recent_following_user8.append(new_follower)


time.sleep(40)

recent_following_user9=[]
user_9="0xLordAlpha"
for user in tweepy.Cursor(api.friends, screen_name=user_9).items(10):
    new_follower=str(user.screen_name)
    recent_following_user9.append(new_follower)


time.sleep(40)


recent_following_user10=[]
user_10="SillyPunts"
for user in tweepy.Cursor(api.friends, screen_name=user_10).items(10):
    new_follower=str(user.screen_name)
    recent_following_user10.append(new_follower)

time.sleep(40)



recent_following_user11=[]
user_11="0xShual"
for user in tweepy.Cursor(api.friends, screen_name=user_11).items(10):
    new_follower=str(user.screen_name)
    recent_following_user11.append(new_follower)
time.sleep(40)


recent_following_user12=[]
user_12="fomosaurus"
for user in tweepy.Cursor(api.friends, screen_name=user_12).items(10):
    new_follower=str(user.screen_name)
    recent_following_user11.append(new_follower)
time.sleep(40)


recent_following_user13=[]
user_13="wassiecapital"
for user in tweepy.Cursor(api.friends, screen_name=user_13).items(10):
    new_follower=str(user.screen_name)
    recent_following_user11.append(new_follower)
time.sleep(40)

recent_following_user14=[]
user_14="Ace_da_Book"
for user in tweepy.Cursor(api.friends, screen_name=user_14).items(10):
    new_follower=str(user.screen_name)
    recent_following_user11.append(new_follower)
time.sleep(40)




time.sleep(40)



#calling main function

while True:
    print("collected initial datas")
    time.sleep(119)
    check_for_followers(api,recent_following_user1,user_1,recent_following_user2,user_2,recent_following_user3,user_3,recent_following_user4,user_4,recent_following_user5,user_5,recent_following_user6,user_6,recent_following_user7,user_7,recent_following_user8,user_8,recent_following_user9,user_9,recent_following_user10,user_10,recent_following_user11,user_11,recent_following_user12,user_12,recent_following_user13,user_13,recent_following_user14,user_14)
    time.sleep(10*5)
print('\n\n\n                   finished following all                           ')

