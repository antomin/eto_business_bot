from asgiref.sync import sync_to_async

from course_app.models import Course, CourseCategory
from service_app.models import ServiceCategory, ServiceSubCategory, ServiceUser


async def get_service_categories():
    return ServiceCategory.objects.filter(is_active=True)


async def get_service_subcategories(category_id):
    return ServiceSubCategory.objects.filter(category=category_id, is_active=True)


async def get_services(subcategory_id):
    return ServiceUser.objects.filter(sub_category=subcategory_id, is_active=True)


@sync_to_async
def check_access(username):
    return username in ServiceUser.objects.filter(is_active=True).values_list('tg', flat=True)


async def get_topservices():
    return ServiceUser.objects.filter(is_active=True, is_top=True)


async def get_course_categories():
    return CourseCategory.objects.filter(is_active=True)


async def get_courses(category_id):
    return Course.objects.filter(category=category_id, is_active=True)
