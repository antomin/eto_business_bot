from asgiref.sync import sync_to_async

from service_app.models import ServiceCategory, ServiceSubCategory, ServiceUser


async def get_service_categories():
    return ServiceCategory.objects.filter(is_active=True)


async def get_service_subcategories(category_id):
    return ServiceSubCategory.objects.filter(category=category_id, is_active=True)


async def get_services(sub_category_id):
    return ServiceUser.objects.filter(sub_category=sub_category_id, is_active=True)


def get_service(service_id):
    return ServiceUser.objects.filter(id=service_id, is_active=True).first()
