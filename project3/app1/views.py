from django.shortcuts import render,redirect
from django.http import HttpResponse
from . form import Detailsform
from . models import Details
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Detailsform(request.POST)
        if form.is_valid():
            #form.save()
            n=form.cleaned_data['name']
            a=form.cleaned_data['age']
            e=form.cleaned_data['email']
            sql = Details(name=n,age=a,email=e)
            sql.save()
            subject = 'welcome G'
            message = f'Hi {n}, thank you for registering.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [e, ]
            send_mail( subject, message, email_from, recipient_list )

            return redirect('/')
    else:
        form = Detailsform()
    return render(request,'index.html',{'form':form})
