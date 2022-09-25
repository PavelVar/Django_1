from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Название статьи по умолчанию')
    anons = models.CharField('Анонс', max_length=250, default='Анонс по умолчанию')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return f'News: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

