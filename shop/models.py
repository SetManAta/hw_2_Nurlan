from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name="Наименование товара")
    price = models.IntegerField(verbose_name="Цена товара")

    def __str__(self):
        return f'{self.name}'

class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name="ФИО клиента")
    age = models.IntegerField(verbose_name="Возвраст клиента")
    item = models.ForeignKey(Item,on_delete=models.CASCADE, related_name="purchases")
    date_purchase = models.DateField(auto_now_add=True, verbose_name='дата покупки')