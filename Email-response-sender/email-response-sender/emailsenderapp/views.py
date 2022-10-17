from django.shortcuts import render
from django.core.mail import send_mail
from emailsender.settings import EMAIL_HOST_USER

# Create your views here.
def query(request):
    if(request.method=="POST"):
        data=request.POST
        email=data.get("email")
        city=data.get("city")
        state=data.get("state")
        zip=data.get("zip")
        query=data.get("query")
        es=data.get("es")
        l=['email']
        send_mail(
        'query',
        f" email:{email}\n city:{city} \n state:{state} \n zip:{zip} \n query:{query} \n es:{es}",
        EMAIL_HOST_USER,
        l,
        fail_silently=False
        )
       
        if(es=="on"):
            send_mail(
            'query',
            f"this is your response \n email:{email}\n city:{city} \n state:{state} \n zip:{zip} \n query:{query}",
            EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
    #print(es)
    return render(request,"query.html")

