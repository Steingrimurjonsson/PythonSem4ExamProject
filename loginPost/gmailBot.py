import smtplib

class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + "ssskjskj@gmail.com", "steingrimurkj@gmail.com", "steinautomate@gmail.com",
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            ["ssskjskj@gmail.com", "steingrimurkj@gmail.com", "steinautomate@gmail.com"],
            headers + "\r\n\r\n" + body)
