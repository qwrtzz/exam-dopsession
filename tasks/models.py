from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', 'Низкий'
        MEDIUM = 'medium', 'Средний'
        HIGH = 'high', 'Высокий'

    class Status(models.TextChoices):
        PENDING = 'pending', 'К выполнению'
        IN_PROGRESS = 'in_progress', 'В процессе'
        COMPLETED = 'completed', 'Выполнено'

    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание', blank=True)
    priority = models.CharField('Приоритет', max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    status = models.CharField('Статус', max_length=15, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        ordering = ['-created_at']  # сортировка по умолчанию (новые сверху)

    def __str__(self):
        return self.title