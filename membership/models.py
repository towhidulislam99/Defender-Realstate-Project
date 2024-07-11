from django.db import models
from ckeditor.fields import RichTextField

class Membership(models.Model):
    title = models.CharField(max_length=500)  
    description = RichTextField()
    facilities = RichTextField()
    image = models.ImageField(upload_to='Membership/', blank=True, null=True)  

    def __str__(self):
        return self.title
    
    @property
    def description_list(self):
        if self.facilities:
            return [item.strip() for item in self.facilities.split('|')]
        return []

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"  
        