from django.db import models

# Create your models here.

class TblContact(models.Model):
    """Model representing a email of company (e.g. a@a.com)."""
    email = models.EmailField(  
        max_length=254,     
        help_text="Enter a email of company (e.g. a@a.com)"
        )
    """Model representing a mobile of company (e.g. +919898257016)."""
    mobile = models.CharField(  
        max_length=20,  
        unique=True,   
        help_text="Enter a mobile of company (e.g. +919898257016)"
        )    

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "%s %s" %(self.email, self.mobile)

class TblSlider(models.Model):
    """Model representing a email of slider (e.g. Best Company)."""
    title = models.CharField(  
        max_length=100,     
        help_text="Enter a title of slider (e.g. Best Company)"
        )
    
    """Model representing a description of slider (e.g. a@a.com)."""
    description = models.TextField(  
        max_length=500,     
        help_text="Enter a description of Slider (e.g. any)"
        )
    """Model representing a image of slider (e.g. .jpg)."""
    sliderimage = models.FileField(upload_to='images/')  # for creating file input
       

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "%s" %(self.title)        


class TblTeam(models.Model):
    """Model representing a name of team member (e.g. Ronak Panchal)."""
    name = models.CharField(max_length=100, help_text="Enter a name (e.g. Ronak Panchal)")
    """Model representing a designation of team member (e.g. Software Engineer)."""
    designation = models.CharField(max_length=100, help_text="Enter a designation (e.g. Web Designer)")
    """Model representing a qualification of team member (e.g. MCA, BTech)."""
    qualification = models.TextField(max_length=100, help_text="Enter a qualification (e.g. MCA, BTech)") 
    """Model representing a facebook link (e.g. fb/ronak)."""
    social_fb = models.TextField(max_length=500, help_text="Enter a facebook link (e.g. fb/ronak)")
    
    """Model representing a linkedin link (e.g. ln/ronak)."""
    social_ln = models.TextField(max_length=500, help_text="Enter a linkedin link (e.g. Best Company)")
    
    """Model representing a instagram link (e.g. insta/ronak)."""
    social_insta = models.TextField(max_length=500, help_text="Enter a instagram link (e.g. Best Company)")
    
    """Model representing a twitter link (e.g. @twitter/ronak)."""
    social_twitter = models.TextField(max_length=500, help_text="Enter a twitter link (e.g. Best Company)")
    
    """Model representing a photo of team member (e.g. .jpg)."""
    sliderimage = models.FileField(upload_to='photo/')  # for creating file input
       

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "%s" %(self.name)        


class TblTestimonial(models.Model):
    """Model representing a name of testimonial (e.g. Ronak Panchal)."""
    title = models.CharField(max_length=100, help_text="Enter a name (e.g. Ronak Panchal)")
    """Model representing a designation of team member (e.g. Software Engineer)."""
    designation = models.CharField(max_length=100, help_text="Enter a designation (e.g. Web Designer)")  
    """Model representing a designation of team member (e.g. Software Engineer)."""
    description = models.TextField(max_length=500, help_text="Enter a description (e.g. Brief)")
    """Model representing a photo of team member (e.g. .jpg)."""
    photoimage = models.FileField(upload_to='testimonialphoto/')  # for creating file input
       

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "%s" %(self.title)       


# Enquiry -> name, email, mobileno, subject(default: Enquiry for Web Solution)
# ContactUs -> name, email, mobileno, servicename, budget if, project details
# Potfolio -> title, potfolioimage, navigatelink, description
# Blog -> 
# Events -> eventname, eventimage(multiple), created