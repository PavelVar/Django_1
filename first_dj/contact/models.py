from django.db import models


class Message(models.Model):
    name = models.CharField('Name', max_length=20)
    email = models.CharField('E-mail', max_length=50)
    text = models.TextField('Статья')

    def __str__(self):
        return f'Message: {self.name} | {self.email}'

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
