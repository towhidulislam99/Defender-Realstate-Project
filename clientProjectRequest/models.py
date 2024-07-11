from django.db import models
from ckeditor.fields import RichTextField
from project.models import Project

class ClientProjectRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = RichTextField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client Project Request"
        verbose_name_plural = "Client Project Requests"
        
        
