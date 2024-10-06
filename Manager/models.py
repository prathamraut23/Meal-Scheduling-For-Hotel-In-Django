from django.db import models

# Create your models here.
class menu_card(models.Model):
    dish_id=models.IntegerField(null=True)
    dish_name=models.CharField(max_length=50)
    dish_price=models.CharField(max_length=10)
    dish_category=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images",default="")
    def __str__(self):
        return self.dish_name

class Order(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(default=' ',max_length=100)
    phoneno=models.IntegerField(default=0,max_length=10)
    orderdate=models.CharField(default=' ',max_length=50)
    sheduletime=models.CharField(default=' ',max_length=50)
    dish_list=models.CharField(default=' ',max_length=1000)
    quantity_list=models.CharField(default=' ',max_length=1000)
    price_list=models.CharField(default=' ',max_length=1000)
    members=models.IntegerField(default=0,max_length=2)
    total=models.IntegerField(default=0,max_length=10)
    def __str__(self):
        return str(self.fullname)+str(self.phoneno)