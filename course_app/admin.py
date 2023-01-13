from django.contrib import admin

from course_app.models import Course, CourseCategory

admin.site.register(CourseCategory)
admin.site.register(Course)
