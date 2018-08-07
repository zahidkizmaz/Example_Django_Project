from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from myapp.forms import ContactForm

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)

def form_example(request):
    form = ContactForm()
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = ['info@example.com']
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect('/thanks/')
    return render(request, 'myapp/form_example.html', {'form' : form})