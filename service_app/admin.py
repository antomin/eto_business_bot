from django.contrib import admin
from django.utils.safestring import mark_safe

from service_app.models import ServiceCategory, ServiceSubCategory, ServiceUser


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_active',)
    list_filter = ('is_active',)


class ServiceSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_active',)
    list_filter = ('category', 'is_active')


class ServiceUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created_at', 'updated_at', 'is_top', 'is_active')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_editable = ('is_top', 'is_active')
    list_filter = ('is_top', 'is_active')
    fields = ('first_name', 'last_name', 'sub_category', 'description', 'image_url', 'phone', 'email', 'tg', 'web_url',
              'is_top', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceSubCategory, ServiceSubCategoryAdmin)
admin.site.register(ServiceUser, ServiceUserAdmin)

admin.site.site_title = '@eto_business_bot'
admin.site.site_header = 'Администрирование @eto_business_bot'
admin.site.site_url = None
