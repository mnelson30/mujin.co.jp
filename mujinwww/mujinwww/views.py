# -*- coding: utf-8 -*-
# Copyright (C) 2013 MUJIN Inc
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.conf import settings

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = settings.EMAIL_HOST_USER
gmail_pwd = settings.EMAIL_HOST_PASSWORD

from django.shortcuts import render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.utils.translation import get_language_from_request
from django.conf import settings

from . import models

def mail(to, subject, text, attach=None, from_address=gmail_user):
    msg = MIMEMultipart()

    msg['From'] = from_address
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text, 'html'))
    #~ msg.attach(MIMEText(text, 'plain'))

    if attach is not None:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(gmail_user, gmail_pwd)
    mail_server.sendmail(gmail_user, to, msg.as_string())
    mail_server.close()

def sendinquiry(request):
    #~ from IPython.Shell import IPShellEmbed; IPShellEmbed(argv='')(local_ns=locals())
    if request.method == 'POST':
        to = 'info@mujin.co.jp'

        subject = 'New inquiry from ' + request.POST['first_name'] + ' ' + request.POST['last_name']

        request_dict = {}
        for k, v in request.POST.iteritems():
            request_dict[k] = v.encode('utf-8')

        text = '''
<h1>New inquiry from {first_name} {last_name}</h1>
<br />
<b>Their info:</b>
<ul>
  <li>Name: {first_name} {last_name}</li>
  <li>Email: {email}</li>
  <li>Company: {company_name}</li>
  <li>Address: {address}</li>
  <li>City: {city}</li>
  <li>State/Prefecture: {state}</li>
  <li>Country: {country}</li>
  <li>Telephone: {telephone}</li>
</ul>
<br>
<b>What they said:</b>
<p>
  {message}
</p>
        '''.format(**request_dict)

        mail(to, subject, text, from_address=request.POST['email'])
    return HttpResponse()

def catchallhtml(request, name):
    try:
        return render_to_response(name + '.html', RequestContext(request))
    except TemplateDoesNotExist:
        return index(request)

def get_translated_news(request, news):
    ret = []
    LANG = get_language_from_request(request)[:2].lower()
    for newsitem in news:
        this_newsitem = {'en_title': newsitem.en.title}
        this_newsitem['pub_date'] = newsitem.pub_date.strftime('%b %d, %Y')
        if LANG == 'ja':
            this_newsitem['title'] = newsitem.ja.title
            this_newsitem['content'] = newsitem.ja.content
        else:
            # always fallback on english
            this_newsitem['title'] = newsitem.en.title
            this_newsitem['content'] = newsitem.en.content
        ret.append(this_newsitem)
    return ret

def index(request):
    news = models.NewsEntry.objects.all().order_by('-pub_date')[:4]
    template = {'news': get_translated_news(request, news)}
    return render_to_response('index.html', RequestContext(request, template))

def news(request):
    news = models.NewsEntry.objects.all().order_by('-pub_date')
    template = {'news': get_translated_news(request, news)}
    return render_to_response('news.html', RequestContext(request, template))

def ignore(request,*args,**kwargs):
    return HttpResponseNotFound()
