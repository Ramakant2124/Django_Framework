from django.db import models

# Create your models here.
class LaptopModel(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="media/")

def __str__(self):
        return f'{self.brand} {self.model}'