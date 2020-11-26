from django.shortcuts import render,get_object_or_404
from .forms import rooba
from django.views.generic import DetailView, ListView
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

# about view    
def about(request):
    files2 = client.objects.all()
    files1 = service.objects.all()
    data ={
        "clin" :files2,
        "serv" : files1,
        "title" : "About | "
    }
    return render(request,'about.html', data)

# gallery view
class GalleryView(ListView):
    model = gallery
    context_object_name = 'gallery' 
    data = gallery.objects.all().order_by('-date')
    template_name = 'gallery.html'

    def get_context_data(self, *args, **kwargs):
        data = super(GalleryView, self).get_context_data(*args,  **kwargs)
        data['title'] = 'Gallery | '
        serv = service.objects.all()
        data['serv'] = serv
        return data


# blog view


class BlogView(ListView):
    model = blog
    context_object_name = 'blogs' 
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        data = super(BlogView, self).get_context_data(*args,  **kwargs)
        data['title'] = 'Blogs | '
        serv = service.objects.all()
        data['serv'] = serv
        bloger = blog.objects.all().order_by('-date')
        data['blogs'] = bloger
        return data

# blog detail view

class BlogDetailView(DetailView):
    model = blog
    template_name = 'blog-single.html'
    data = blog.objects.all()
    context_object_name = 'blog'

    def get_context_data(self, *args, **kwargs):
        data = super(BlogDetailView, self).get_context_data(*args,  **kwargs)
        data['title'] = 'Blogs | '
        serv = service.objects.all()
        data['serv'] = serv
        blogs = blog.objects.all().order_by('-date')
        data['blogs'] = blogs
        return data

# service view

class ServiceView(ListView):
    model = service
    
    context_object_name = 'servs'   
    data = service.objects.all()
    template_name = 'services.html'  

    def get_context_data(self, *args, **kwargs):
        data = super(ServiceView, self).get_context_data(*args, **kwargs)
        data['title'] = 'Services | '
        serv = service.objects.all()
        data['serv'] = serv
        return data

# service detail view

class Service_detail(DetailView):
    
    model = service
    template_name = 'service_detail.html'
    context_object_name = 'servs'
    data = service.objects.all()
    def get_context_data(self, *args, **kwargs):
        data = super(Service_detail, self).get_context_data(*args, **kwargs)
        data['title'] = 'Services | '
        serv = service.objects.all()
        data['serv'] = serv
        return data


# contact view

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
            "title" : "Contact | "
                    
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
            "title" : "Contact | "
                    
            }
        return render(request, 'contact.html',data)






   

   
