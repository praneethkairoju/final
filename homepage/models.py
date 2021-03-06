from django.db import models
from django.db.models.signals import pre_save
from sdrkproject.utils import unique_slug_generator
# Create your models here.




# services 

class service(models.Model):
     title = models.CharField(max_length=30)
     images = models.ImageField(upload_to='pics')
     slug = models.SlugField(max_length=250, null=True, blank=True)
     description = models.TextField()
     shortlist = models.BooleanField(default=False)

     


# testimonials

class client(models.Model):
     images = models.ImageField(upload_to='pics')
     name = models.CharField(max_length=20)
     description = models.TextField()
     designation = models.CharField(max_length=200)

     


     

#gallery

class gallery(models.Model):
     images = models.ImageField(upload_to='pics')
     date = models.DateTimeField(auto_now_add=True)
     description = models.CharField(max_length=30)
     



# blog

class blog(models.Model):
     images = models.ImageField(upload_to='pics')
     title = models.CharField(max_length=20)
     description = models.TextField()
     slug = models.SlugField(max_length=250, null=True, blank=True)
     author = models.CharField(max_length=20)
     date = models.DateTimeField(auto_now_add=True)
     
     

# comments

class comment(models.Model):
     name = models.CharField(max_length=20)
     date = models.DateTimeField(auto_now_add=True)
     comment = models.TextField()


class contactform(models.Model):    
    name = models.CharField(max_length=30)
    email =models.EmailField() 
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=60)
    message = models.TextField()

    
def slug_generator(sender ,instance, *args, **kwargs):
     if not instance.slug:
          instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender= service)
pre_save.connect(slug_generator, sender= blog)