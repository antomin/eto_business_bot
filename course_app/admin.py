from django.contrib import admin

from course_app.models import Course, CourseCategory


class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_active',)
    list_filter = ('is_active',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_active',)
    list_filter = ('category', 'is_active',)
    fields = ('title', 'category', 'description', 'image_url', 'url', 'is_active', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(Course, CourseAdmin)
