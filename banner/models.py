from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=500)
    discount = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Banner/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"