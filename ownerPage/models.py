from django.db import models
from django.contrib.auth.models import User


class Owners(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notice = models.TextField(max_length=500, blank=True)

    cpu = models.TextField(max_length=50, blank=True)
    main_board = models.TextField(max_length=50, blank=True)
    memory = models.TextField(max_length=50, blank=True)
    graphic_card = models.TextField(max_length=50, blank=True)
    ssd = models.TextField(max_length=50, blank=True)
    mouse = models.TextField(max_length=50, blank=True)
    keyboard = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username