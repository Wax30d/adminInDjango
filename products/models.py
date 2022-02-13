from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    mfg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def show_desc(self):
        return self.description[:50]
