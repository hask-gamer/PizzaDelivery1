from django.db import models
from django.contrib.auth.models import User


class Filial(models.Model):
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address

class Pizza(models.Model):

    PIZZA_SIZE = (
        ('kichi_25', 'Kichi(25)'),
        ('ortancha_35', 'Ortancha(35)'),
        ('katta_45', 'Katta(45)'),
    )
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    size = models.CharField(max_length=50, choices=PIZZA_SIZE)
    is_available = models.BooleanField(default=True)
    ingredients = models.TextField()
    image = models.ImageField(upload_to='pizza_image/')

    def __str__(self):
        return self.name
    

class Order(models.Model):

    STATUS = (
        ('Tayyorlanyapti', 'Tayyorlanyapti'),
        ('Kuryerga berildi', 'Kuryerga berildi'),
        ('Kuryer yolda', 'Kuryer yolda'),
        ('Bekor qilindi', 'Bekor qilindi'),
        ('Yetkazildi', 'Yetkazildi'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=150)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.user
