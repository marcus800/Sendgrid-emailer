# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid.helpers.mail import *
import random
import urllib2 as urllib
import urllib
import datetime



class SendgridEmailer:
    def __init__(self, apikey):
        self.apikey = apikey
        self.sg = sendgrid.SendGridAPIClient(apikey=apikey)

    def sendEmail(self, new_to_email, new_from_email, new_name, html):



        from_email = Email(new_from_email)
        to_email = Email(new_to_email)
        subject = "Open me" + str(random.randrange(0, 1000))
        content = Content("text/html",html) #<-- the html is all the html that will be in the email



        mail = Mail(from_email, subject, to_email, content)
        mail.personalizations[0].add_substitution(Substitution("-name-", new_name))
        mail.personalizations[0].add_substitution(Substitution("-datetime-", datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")))


        #mail.template_id = "1726f67a-99ae-429c-b59d-572771cb7d1c" <-- sendgrid template


        self.sg.client.mail.send.post(request_body=mail.get())







#The Template1Example.html will be the HTML to be sent.
