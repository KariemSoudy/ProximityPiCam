#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "tt3724522@gmail.com"
frompass = "kariem_2000"
toaddr = "aj.bsb7@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Message From Raspberry Pi"
body = '<h1>This is an extended email test From Raspberry Pi</h1>'
msg.attach(MIMEText(body, 'html'))

filename = "pi.jpg"
attachment = open("pi.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= {}".format(filename))
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587) #587 or 465
server.ehlo()
server.starttls()
server.ehlo()
server.login('tt3724522@gmail.com', 'kariem_2000')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()