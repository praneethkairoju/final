from django.shortcuts import render
from .forms import rooba
from django.views.generic import DetailView
from .models import service, client, gallery,blog, contactform
from django.core.mail import send_mail


# Create your views here.


def index(request):
    
    files1 = service.objects.all()
    files2 = client.objects.all()
    files3 = blog.objects.all().order_by('-date')[:3]
    files4 = rooba
    
    
    if request.method == 'POST':

        given_name = request.POST['name']
        given_email = request.POST['email']
        given_phone = request.POST['phone']
        given_subject = request.POST['subject']
        given_message = request.POST['message']
        data = {
            "serv" : files1,
            "clin": files2,
            "blog": files3,
            "form":files4,
            "thank" :"Thanks You , We will Respond Soon.."
                  
            }
        
        send_mail(
            given_subject , # subject
            'My name is' +' ' +given_name +' ' +'my mobile' + ' '+ given_phone +'  '+'{' +given_message +'}', # message
            given_email, # from email

            ['harinath2000jangon@gmail.com'], # to email
            
        )    
        return render(request, 'index.html', data)
    else:

        data = {
            "serv" : files1,
            "clin": files2,
            "blog": files3,
            "form": files4,
                    
            }
        return render(request, 'index.html',data)
          
def about(request):
    files2 = client.objects.all()
    files1 = service.objects.all()
    data ={
        "clin" :files2,
        "serv" : files1,
        "title" : "About |"
    }
    return render(request,'about.html', data)


def photos(request):
    files4 = gallery.objects.all()
    files1 = service.objects.all()

    data = {
        "photos" : files4,
        "serv" : files1,
        "title" : "Gallery |"
    }
    return render(request,'gallery.html', data)



def blogs(request):
    files3 = blog.objects.all().order_by('-date')[:6]
    files1 = service.objects.all()

    data = {
        "blog":files3,
        "serv" : files1,
        "title" : "Blogs |"
    }
    

    return render(request,'blog.html', data)


def services(request):
    files1 = service.objects.all()
    data ={
        "serv" :files1,
        "title" : "Services |"
    }
    return render(request,'services.html',data)



def Contact(request):
    files1 = service.objects.all()
    files4 = rooba
    
    if request.method == 'POST':

        given_name = request.POST['name']
        given_email = request.POST['email']
        given_phone = request.POST['phone']
        given_subject = request.POST['subject']
        given_message = request.POST['message']
        data = {
            "form":files4,
            "serv" : files1,
            "thank" :"Thanks You , We will Respond Soon..",
            "title" : "Contact "
                    
            }
        
        send_mail(
            given_subject , # subject
            'My name is' +' ' +given_name +' ' +'my mobile' + ' '+ given_phone +'  '+'{' +given_message +'}', # message
            given_email, # from email
            ['harinath2000jangon@gmail.com'], # to email
            
        )    
        return render(request, 'contact.html', data)
    else:

        data = {
            
            "form": files4,
            "serv" : files1,
            "title" : "Contact |"
                    
            }
        return render(request, 'contact.html',data)
    
def blogsigle(request):
    files1 = service.objects.all()
    files3 = blog.objects.all().order_by('-date')

    data = {
        "blog":files3,
        "serv" : files1,
        "title" : "Blog Details"
    }
    return render(request, 'blog-single.html', data)

