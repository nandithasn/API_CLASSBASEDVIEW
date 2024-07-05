from django.db import models

# Create your models here.
class Productcategory(models.Model):
    category_name=models.CharField(max_length=100,primary_key=True)
    category_id=models.IntegerField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_name=models.ForeignKey(Productcategory,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    pid=models.IntegerField()
    price=models.IntegerField()
    date=models.DateField()


    def __str__(self):
        return self.pname