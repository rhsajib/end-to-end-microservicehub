from django.db import models


class Messages(models.Model):
    message = models.TextField(blank=True, null=True)