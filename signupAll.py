from secrets import secretPassword, secretEmail, secretFirstname, secretLastname, secretUsername
from signup.facebookSignup import FacebookSignUpBot
from signup.twitterSignup import TwitterSignUpBot


#AUTO SIGNS UP TO YOUR FACEBOOK TWITTER AND INSTAGRAM ACCOUNTS

class easySignupSocialMediaBot():
    def __init__(self):

        #ERROR WITH FB SIGNUP
        #FacebookSignUpBot(secretFirstname, secretLastname, secretEmail, secretPassword)
        #print('fb done')

        TwitterSignUpBot(secretUsername, secretEmail, secretPassword)
        print('twiiter done')

def main():
    easySignupSocialMediaBot()

if __name__ == '__main__':
    main()
