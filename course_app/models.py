from django.db import models


class CourseCategory(models.Model):
    title = models.CharField(verbose_name='категория', max_length=24)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Course(models.Model):
    title = models.CharField(verbose_name='название', max_length=24)
    category = models.ForeignKey(CourseCategory, verbose_name='категория', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='описание')
    url = models.URLField(verbose_name='ссылка')
    image_url = models.ImageField(upload_to='service_images', verbose_name='изображение', max_length=64)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f'{self.title} ({self.category})'

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
