from django.db import models

# Create your models here.




# services 

class service(models.Model):
     images = models.ImageField(upload_to='pics')
     servicename = models.CharField(max_length=20)
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
     author = models.CharField(max_length=20)
     date = models.DateTimeField(auto_now_add=True)
     shortlist = models.BooleanField(default=False)
     

# comments

class comment(models.Model):
     name = models.CharField(max_length=20)
     date = models.DateTimeField(auto_now_add=True)
     comment = models.TextField()
