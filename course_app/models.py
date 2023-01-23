from django.db import models


class CourseCategory(models.Model):
    title = models.CharField(verbose_name='категория', max_length=128)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-is_active', 'title']


class Course(models.Model):
    title = models.CharField(verbose_name='название', max_length=128)
    category = models.ForeignKey(CourseCategory, verbose_name='категория', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='описание')
    url = models.URLField(verbose_name='ссылка')
    image_url = models.ImageField(upload_to='course_img', default='course_img/default.jpg', verbose_name='изображение',
                                  max_length=256)
    is_active = models.BooleanField(verbose_name='активна', default=True)
    created_at = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='последнее обновление', auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.category})'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-is_active', 'updated_at']
