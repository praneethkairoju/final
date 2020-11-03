from django.contrib import admin
from .models import service,client,gallery,blog,comment,contactform

# Register your models here.


admin.site.site_header = "SDRK Tecnologies Admin Panel"

#services admin 
class serviceAdmin(admin.ModelAdmin):
    list_display = ('servicename', 'shortlist')

admin.site.register(service,serviceAdmin)


#client admin
class clientadmin(admin.ModelAdmin):
    list_display = ('name', 'designation')

admin.site.register(client,clientadmin)

#blog admin
class blogadmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)

admin.site.register(blog,blogadmin)

#gallery admin
class galleryadmin(admin.ModelAdmin):
    list_display = ('description', 'date')

admin.site.register(gallery,galleryadmin)

#comment admin
class commentadmin(admin.ModelAdmin):
    list_display = ('name', 'date')

admin.site.register(comment,commentadmin)

admin.site.register(contactform)