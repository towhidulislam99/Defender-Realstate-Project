from django.db import models
from project.models import Project

class ProjectSummary(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    icon = models.CharField(max_length=300)
    number = models.IntegerField()
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project Summary"
        verbose_name_plural = "Project Summaries"