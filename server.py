from flask import Flask, request, send_from_directory

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

if os.path.exists('/var/mujinmanager_gmailpass'):
    EMAIL_HOST_PASSWORD=open('/var/mujinmanager_gmailpass','r').read()
else:
    EMAIL_HOST_PASSWORD=''
EMAIL_HOST_USER='mujinmanager@gmail.com'

def mail(subject, text):
    msg = MIMEMultipart()

    msg['From'] = EMAIL_HOST_USER
    msg['To'] = 'info@mujin.co.jp'
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'html'))

    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    mail_server.sendmail(EMAIL_HOST_USER, msg['To'], msg.as_string())
    mail_server.close()

app = Flask(__name__)

"""
@app.route('/')
def derp():
    return site('index.html')

@app.route('/<path:filename>')
def site(filename):
    return send_from_directory(app.root_path + '/_site/', filename)
"""

@app.route('/contactSubmit', methods=['POST'])
def contact():
    mail(unicode(request.json['subject']).encode('utf-8'), unicode(request.json['body']).encode('utf-8'))
    return '{}'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
