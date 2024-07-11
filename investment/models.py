from django.db import models
from ckeditor.fields import RichTextField


class Investment(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = RichTextField()
    image = models.ImageField(upload_to='investment/', blank=True, null=True)

    def __str__(self):
        return self.title or 'No Title'
    
    @property
    def description_list(self):
        if self.description:
            return [item.strip() for item in self.description.split('|')]
        return []

    class Meta:
        verbose_name = "Investment"
        verbose_name_plural = "Investments"


class InvestmentTwo(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = RichTextField()
    image = models.ImageField(upload_to='investment_Two/', blank=True, null=True)

    def __str__(self):
        return self.title or 'No Title'
    
    @property
    def description_list(self):
        if self.description:
            return [item.strip() for item in self.description.split('|')]
        return []

    class Meta:
        verbose_name = "Investment Two"
        verbose_name_plural = "Investments Two"


class InvestmentThree(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = RichTextField()
    image = models.ImageField(upload_to='investment_Three/', blank=True, null=True)

    def __str__(self):
        return self.title or 'No Title'
    
    @property
    def description_list(self):
        if self.description:
            return [item.strip() for item in self.description.split('|')]
        return []

    class Meta:
        verbose_name = "Investment Three"
        verbose_name_plural = "Investments Three"

# class Investment(models.Model):
#     title = models.CharField(max_length=500, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     image = models.ImageField(upload_to='investment/', blank=True, null=True)

#     def __str__(self):
#         return self.title or 'No Title'
    
#     @property
#     def description_list(self):
#         if self.description:
#             return [item.strip() for item in self.description.split(',')]
#         return []


#     class Meta:
#         verbose_name = "Investment"
#         verbose_name_plural = "Investments"


# # class DescriptionInvestmentOne(models.Model):
# #     description = models.CharField(max_length=500, blank=True, null=True)

# #     class Meta:
# #         verbose_name = "Investment Description One"
# #         verbose_name_plural = "Investment Description One"


# class InvestmentTwo(models.Model):
#     title = models.CharField(max_length=500, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     image = models.ImageField(upload_to='investment_Two/', blank=True, null=True)

#     def __str__(self):
#         return self.title or 'No Title'
    
#     @property
#     def description_list(self):
#         if self.description:
#             return [item.strip() for item in self.description.split(',')]
#         return []

#     class Meta:
#         verbose_name = "Investment Two"
#         verbose_name_plural = "Investments Two"


# # class DescriptionInvestmentTwo(models.Model):
# #     description = models.CharField(max_length=500, blank=True, null=True)

# #     class Meta:
# #         verbose_name = "Investment Description Two"
# #         verbose_name_plural = "Investment Description Two"


# class InvestmentThree(models.Model):
#     title = models.CharField(max_length=500, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     image = models.ImageField(upload_to='investment_Three/', blank=True, null=True)

#     def __str__(self):
#         return self.title or 'No Title'
    
#     @property
#     def description_list(self):
#         if self.description:
#             return [item.strip() for item in self.description.split(',')]
#         return []

#     class Meta:
#         verbose_name = "Investment Three"
#         verbose_name_plural = "Investments Three"


# class DescriptionInvestmentThree(models.Model):
#     description = models.CharField(max_length=500, blank=True, null=True)

#     class Meta:
#         verbose_name = "Investment Description Three"
#         verbose_name_plural = "Investment Description Three"
        
class ManualTest(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='investment/', blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title or 'No Title'
    
    @property
    def description_list(self):
        if self.description:
            return [item.strip() for item in self.description.split(',')]
        return []

    class Meta:
        verbose_name = "ManualTest"
        verbose_name_plural = "ManualTest"

