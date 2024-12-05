from django.db import models
from django.utils.translation import gettext_lazy as _

class ToDo(models.Model):
    class StatusChoices(models.TextChoices):
        OPEN = 'OPEN', _('Open')
        WORKING = 'WORKING', _('Working')
        PENDING_REVIEW = 'PENDING_REVIEW', _('Pending Review')
        COMPLETED = 'COMPLETED', _('Completed')
        OVERDUE = 'OVERDUE', _('Overdue')
        CANCELLED = 'CANCELLED', _('Cancelled')

    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.OPEN,
    )

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
