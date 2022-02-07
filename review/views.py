from django.shortcuts import render, redirect

from review.models import Person, Enquiry


# Create your views here.

def feedback(request):
    if(request.POST):
        print(request.POST)
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        occupation=request.POST.get("occupation")
        feedback=request.POST.get('feedback')
        obj=Person(firstname=firstname, lastname=lastname, occupation=occupation, email=email, feedback=feedback)
        obj.save()
        a="Thanks for your Valuable Feedback!"
    
    return render(request, "feedback.html", locals())

def review_page(request):
    objs = Person.objects.all()
    total_entry = len(objs)
    print('total_admission', total_entry)
    return render(request, 'review.html', locals())


def edit_feedback(request):
    
    try:
        obj = Person.objects.get(email=request.user.email)
        if request.POST and obj:
            obj.firstname = request.POST.get('firstname')
            obj.lastname = request.POST.get('lastname')
            obj.email = request.POST.get('email')
            obj.occupation = request.POST.get('occupation')
            obj.feedback = request.POST.get('feedback')
            obj.save()
            print("Edit obj", obj)
            a="Feedback successfully modified."
        else:
            a="Please Login to edit feedback comments"
            return render(request, "feedback.html", locals())
    except:   
        return render(request, "feedback.html", locals())


def deleteDB(request):
    em=request.user.email
    try:
        obj=Person.objects.get(email=em)
        obj.delete()
        return redirect(review_page)
    except:
        return redirect(feedback)
    
#------------------------------------------------------------------


def contactus(request):
    if(request.POST):
        cname=request.POST.get('cname')
        etype=request.POST.get('enquiry_type')
        email=request.POST.get('email')
        econcern=request.POST.get('message')
        obj=Enquiry(cname=cname, etype=etype,email=email, econcern=econcern)
        obj.save()

        a="We got your message, we will be in touch, thank you!"

    return render(request, 'contact.html', locals())