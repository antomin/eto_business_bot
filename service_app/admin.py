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
    fields = ('first_name', 'last_name', 'sub_category', 'description', 'image_url', 'email', 'tg', 'is_top',
              'is_active', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    # def get_html_photo(self, object):
    #     if object.image_url:
    #         return mark_safe(f'<img src="{object.image_url}" width=100')


admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceSubCategory, ServiceSubCategoryAdmin)
admin.site.register(ServiceUser, ServiceUserAdmin)

admin.site.site_title = '@eto_business_bot'
admin.site.site_header = 'Администрирование @eto_business_bot'
admin.site.site_url = None
