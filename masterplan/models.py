from django.db import models
from project.models import Project

class Masterplan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    masterplan_name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='Masterplan/', null=True, blank=True)

    def __str__(self):
        return self.masterplan_name

    class Meta:
        verbose_name = "Masterplan"
        verbose_name_plural = "Masterplans"