from django.contrib import admin
from .models import TeamMember, AboutUs, VideoAboutUs, CeoAboutUs

# Register your models here.
admin.site.register(TeamMember)
admin.site.register(AboutUs)
admin.site.register(VideoAboutUs)
admin.site.register(CeoAboutUs)
