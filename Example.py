import urllib
from sendgrid_emailer import SendgridEmailer


sending = SendgridEmailer("")
sending.sendEmail("example@sentto.com", "example@sendfrom.com", "Bob", urllib.urlopen("Template1Example.html").read())

print(" The email has been sent")
