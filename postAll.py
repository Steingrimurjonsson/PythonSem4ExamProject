from secrets import secretPassword, secretEmail
from loginPost.facebookBot import FacebookBot
from loginPost.twitterBot import TwitterBot
from loginPost.gmailBot import Gmail

#AUTO SIGNS IN TO YOUR FACEBOOK TWITTER AND EMAIL AND SENDS THE SAME POST ON ALL MEDIAS

class easySocialMediaBot():
    def __init__(self, msg, emailSub):
        self.msg = msg
        self.emailsub = emailSub

        myFaceBot = FacebookBot(secretEmail, secretPassword)
        myFaceBot.post_facebook(msg)
        print('fb done')

        myTwitBot = TwitterBot(secretEmail, secretPassword)
        myTwitBot.tweet(msg)
        print('twiiter done')

        myEmailBot = Gmail(secretEmail, secretPassword)
        myEmailBot.send_message(emailSub, msg)
        print("email done")

def main():
    easySocialMediaBot("ENTER YOUR MESSAGE HERE", 'ENTER THE SUBJECT LINE FOR YOUR EMAIL')

if __name__ == '__main__':
    main()
