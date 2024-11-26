from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name