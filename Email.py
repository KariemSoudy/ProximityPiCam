import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Email:

    def __init__(self, _from = "tt3724522@gmail.com", _pass = "kariem_2000", _host = "smtp.gmail.com", _port = 587):
        self.fromaddr = _from
        self.frompass = _pass
        self.host = _host
        self.port = _port


    def sendattachment(self, _to, _subject, _body, _attachment_path):
        #try:
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = _to
        msg['Subject'] = _subject
        body = _body
        msg.attach(MIMEText(body, 'html'))
            
        attachment = open(_attachment_path, "rb")
            
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= {}".format(os.path.split(_attachment_path)[1]))
        msg.attach(part)
            
        server = smtplib.SMTP(self.host, self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.fromaddr, self.frompass)
        text = msg.as_string()
        server.sendmail(self.fromaddr, _to, text)
        server.quit()
        return True

        #except:
            #return False

