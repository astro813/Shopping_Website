from django.db import models

class Cloth(models.Model):
    type = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    material = models.CharField(max_length=250)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.brand + '-' + self.type

class Color(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    sleeve_color = models.CharField(max_length=250)
    body_color = models.CharField(max_length=250)
    nect_line_color = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.body_color