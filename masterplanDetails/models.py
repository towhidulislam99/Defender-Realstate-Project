from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import URLValidator
from project.models import Project
from masterplan.models import Masterplan

class MasterplanDetails(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    masterplan = models.ForeignKey(Masterplan, on_delete=models.CASCADE)
    facilities = RichTextField()
    youtube_url = models.URLField(validators=[URLValidator()])
    image_floorplan = models.ImageField(upload_to='floorplans/')
    floorplan_pdf = models.FileField(upload_to='floorplan/', max_length=100)
    

    def __str__(self):
        return self.masterplan.masterplan_name
    
    @property
    def description_list(self):
        if self.facilities:
            return [item.strip() for item in self.facilities.split('|')]
        return []

    class Meta:
        verbose_name = "Masterplan Detail"
        verbose_name_plural = "Masterplan Details"
        
        
class GalleryImage(models.Model):
    masterplan_detail = models.ForeignKey('MasterplanDetails', related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f"Image for {self.masterplan_detail.masterplan.masterplan_name}"