from django.db import models

class CompanySummary(models.Model):
    title = models.CharField(max_length=500)
    amount = models.IntegerField()  
    icon = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Company Summary"  
        verbose_name_plural = "Company Summaries"  