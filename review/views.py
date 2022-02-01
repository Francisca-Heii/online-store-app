from django.shortcuts import render

from . models import *


# Create your views here.

def review_page(request):
    return render(request, "review.html", locals())


def feedback(request):
    if(request.POST):
        print(request.POST)
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        email=request.POST.get('email')
        occupation=request.POST.get("occupation")
        feedback=request.POST.get('feedback')
        obj=Person(first_name=fname, last_name=lname, email=email, feedback=feedback)
        obj.save()
        r="Thanks for your Valuable Feedback!"
    
    return render(request, "feedback.html", locals())


def contactus(request):
    if(request.POST):
        cname=request.POST.get('cname')
        etype=request.POST.get('enquiry_type')
        email=request.POST.get('email')
        econcern=request.POST.get('message')

        obj=Enquiry(cname=cname, etype=etype,email=email, econcern=econcern)
        obj.save()

        a="Your message was sent, thank you!"

    return render(request, 'contact.html', locals())