# Python Semester 4 Exam Project CPH Business Lyngby Datamatiker
 Social media bots

This project consists of social media bots, where users can post to your social medias from one place. It will log into Facebook, Twitter and Gmail and send/post the desired message. The user will also be able to auto sign up for Twitter. 
The program uses selenium for the main features, smtplib for the email sender.

### Technologies in use:
Selenium 
smtplib
CaptchaSolver(OCR til reCaptcha image)
UserAgent(to fake user agent and make it random)

### User manual
I used pyCharm when making and runnning this project

Make a secrets.py file and replace the fields with your data. Make a new gmail and paste it in the email field. 

```
secretPassword = ‘ENTER PASSWORD’
secretEmail = ‘ENTER GMAIL’
secretFirstname = ‘ENTER FIRST NAME’
secretLastname = ‘ENTER LAST NAME’
secretUsername = ‘ENTER USERNAME’
```

Then enter your message and subject line in postAll.py file

```
	easySocialMediaBot("ENTER YOUR MESSAGE HERE", 'ENTER THE SUBJECT LINE FOR YOUR EMAIL')
```

Or if you want to sign up for Twitter you have to run the signupAll.py file
