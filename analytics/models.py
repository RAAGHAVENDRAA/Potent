# Create your models here.
from django.db import models

class PageView(models.Model):
    page_name = models.CharField(max_length=100, unique=True)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.page_name}: {self.count}"
