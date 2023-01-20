async def generate_service_desc(service):
    text = f'<b>{service.first_name} {service.last_name}</b>\n\n' \
           f'<b>Обо мне:</b>\n{service.description}'

    if service.email:
        text += f'\n\n<b>Email:</b> <code>{service.email}</code>'

    if service.phone:
        text += f'\n\n<b>Тел.:</b> {service.phone}'

    if service.web_url:
        text += f'\n\n<b>Сайт:</b> <a href="{service.web_url}">{service.web_url}</a>'

    return text
