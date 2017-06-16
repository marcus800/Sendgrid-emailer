import urllib
from sendgrid_emailer import SendgridEmailer


sending = SendgridEmailer("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")
sending.sendEmail("example@sentto.com", "example@sendfrom.com", "Bob", urllib.urlopen("Template1Example.html").read())

print(" The email has been sent")