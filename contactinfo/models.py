from django.db import models
from ckeditor.fields import RichTextField
        
class ContactInfo(models.Model):
    name = models.CharField(max_length=200, )
    email = models.EmailField(max_length=254, )
    phone_number_one = models.CharField(max_length=17)
    phone_number_two = models.CharField(max_length=17, blank=True, null=True)
    address = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    instagram_link = models.URLField(max_length=500, blank=True, null=True)
    linkedin_link = models.URLField(max_length=500, blank=True, null=True)
    youtube_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"
        


class UserContact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=17)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Get In Touch"
        verbose_name_plural = "Get In Touch"


class ContactUs(models.Model):
    description = RichTextField()

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"