from django.db import models


class ServiceCategory(models.Model):
    title = models.CharField(verbose_name='категория', max_length=64, unique=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-is_active', 'title']


class ServiceSubCategory(models.Model):
    title = models.CharField(verbose_name='подкатегория', max_length=64, unique=True)
    category = models.ForeignKey(ServiceCategory, verbose_name='категория', on_delete=models.PROTECT)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f'{self.title}({self.category})'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['-is_active', 'title', 'category']


class ServiceUser(models.Model):
    first_name = models.CharField(verbose_name='имя', max_length=24)
    last_name = models.CharField(verbose_name='фамилия', max_length=24)
    image_url = models.ImageField(upload_to='service_img', verbose_name='изображение', max_length=64, blank=True)
    sub_category = models.ManyToManyField(ServiceSubCategory, verbose_name='категории')
    description = models.TextField(verbose_name='описание')
    email = models.EmailField(verbose_name='email', blank=True, unique=True)
    tg = models.CharField(verbose_name='телеграм', max_length=24, blank=True, unique=True)
    is_top = models.BooleanField(verbose_name='топ', default=False)
    is_active = models.BooleanField(verbose_name='активна', default=True)
    created_at = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='последнее обновление', auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    async def get_category_id(self):
        return ServiceCategory.objects.get(id=self.sub_category.first().category.id)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-is_active', 'updated_at']

