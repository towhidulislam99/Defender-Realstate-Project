from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import os
from banner.models import Banner
from companysummary.models import CompanySummary
from masterplan.models import Masterplan
from membership.models import Membership
from clientreview.models import ClientReview
from teammember.models import TeamMember, AboutUs, VideoAboutUs, CeoAboutUs
from contactinfo.models import ContactInfo, ContactUs
from investment.models import Investment,InvestmentTwo,InvestmentThree
from project.models import Project
from projectSummary.models import ProjectSummary
from masterplanDetails.models import MasterplanDetails,GalleryImage



# Create your views here.
def indexpage(request):
    banner_data = Banner.objects.all()
    summary = CompanySummary.objects.all()
    masterplan_data = Masterplan.objects.all()
    membership_data = Membership.objects.all()
    clientreview_data = ClientReview.objects.all()
    teammember_data = TeamMember.objects.all()
    contactinfo_data = ContactInfo.objects.all()
    
    

    data = {
            "banner_data" : banner_data,
            "summary" : summary,  
            "masterplan_data" : masterplan_data,
            "membership_data" : membership_data, 
            "clientreview_data" : clientreview_data, 
            "teammember_data" : teammember_data,
            "contactinfo_data" : contactinfo_data,       
            
           }
    
    return render(request, 'index.html', data)



def convert_to_embed_url(url):
    if 'watch?v=' in url:
        return url.replace('watch?v=', 'embed/')
    return url

def aboutpage(request):
    about_data = AboutUs.objects.all()
    videoabout_data = VideoAboutUs.objects.all()
    ceoabout_data = CeoAboutUs.objects.all()
    teammember_data = TeamMember.objects.all()

    for video in videoabout_data:
        video.video_url = convert_to_embed_url(video.video_url)

    data = {
            "about_data" : about_data,
            "videoabout_data" : videoabout_data,
            "ceoabout_data" : ceoabout_data,
            "teammember_data" : teammember_data,
                
            
           }
    
    return render(request, 'about.html', data)


def projectDetailspage(request):
    banner_data = Banner.objects.all()
    masterplan_data = Masterplan.objects.all()
    project_data = Project.objects.all()
    projectSummary_data = ProjectSummary.objects.all()
    masterplandetails_data = MasterplanDetails.objects.all()
    galleryimage_data = GalleryImage.objects.all()
    siteManager_team_members = TeamMember.objects.filter(position="3")
    

    for video in masterplandetails_data:
        video.youtube_url = convert_to_embed_url(video.youtube_url)

    data = {
            "banner_data" : banner_data,
            "masterplan_data" : masterplan_data,
             "project_data" : project_data,
             "projectSummary_data" : projectSummary_data,
             "masterplandetails_data" : masterplandetails_data, 
             "galleryimage_data" : galleryimage_data,  
             "siteManager_team_members" : siteManager_team_members,       
            
           }
    
    return render(request, 'project_details.html', data)


def investmentpage(request):
    investment_data = Investment.objects.all()
    investmenttwo_data = InvestmentTwo.objects.all()
    investmentthree_data = InvestmentThree.objects.all()
    # investmentdesone_data = DescriptionInvestmentOne.objects.all()
    # investmentdestwo_data = DescriptionInvestmentTwo.objects.all()
    # investmentdesthree_data = DescriptionInvestmentThree.objects.all()
    
    
    

    data = {
            "investment_data" : investment_data,
            "investmenttwo_data" : investmenttwo_data,
            "investmentthree_data" : investmentthree_data,
            # "investmentdesone_data" : investmentdesone_data,
            # "investmentdestwo_data" : investmentdestwo_data,
            # "investmentdesthree_data" : investmentdesthree_data,
                
            
           }
    
    return render(request, 'investment.html', data)

def contactpage(request):
    contactinfo_data = ContactInfo.objects.all()
    contactus_data = ContactUs.objects.all()
   

    data = {
            "contactinfo_data" : contactinfo_data,
            "contactus_data" : contactus_data,
            
           }
    
    return render(request, 'contact.html', data)

def manualpage(request):
    manual_data = ManualTest.objects.all()
   
   

    data = {
            "manual_data" : manual_data,
           
           }
    
    return render(request, 'manual.html', data)
    
    

