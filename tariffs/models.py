from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title[:20]}"
    

class Product(models.Model):

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    fbs = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return f"{self.fbs*100}% : {self.title[:15]}"

    def get_fbs(self):
        return f"{self.fbs*100}%"
