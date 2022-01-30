from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)
    orgin = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}-{self.orgin}'

    def get_absolute_url(self):
        pass


class Product(models.Model):
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=100)
    description = models.TextField(blank=True,default='')
    expir_date = models.DateField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}-{self.kind}-{self.price}-{self.expir_date}'

    def get_absolute_url(self):
        pass




