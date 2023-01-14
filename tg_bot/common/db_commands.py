from asgiref.sync import sync_to_async

from service_app.models import ServiceCategory, ServiceSubCategory, ServiceUser


def get_categories():
    categories = ServiceCategory.objects.filter(is_active=True)
    return categories


async def get_sub_categories(category_id):
    sub_categories = ServiceSubCategory.objects.afilter(category=category_id, is_active=True)
    return sub_categories


async def get_services(sub_category_id):
    services = ServiceUser.objects.filter(sub_category=sub_category_id, is_active=True)
    return services
