from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    task = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Užrašas'
        verbose_name_plural = 'Užrašai'

