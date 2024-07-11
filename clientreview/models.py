from django.db import models

class ClientReview(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='ClientReview/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client Review"  
        verbose_name_plural = "Client Reviews"  