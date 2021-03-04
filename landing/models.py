from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField('Текст новости')
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
