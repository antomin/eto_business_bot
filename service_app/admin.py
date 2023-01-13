from django.contrib import admin

from service_app.models import ServiceCategory, ServiceSubCategory, ServiceUser

admin.site.register(ServiceCategory)
admin.site.register(ServiceSubCategory)
admin.site.register(ServiceUser)
