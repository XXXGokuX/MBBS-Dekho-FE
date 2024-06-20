from django.db import models

# Create your models here.
class College(models.Model):
    college_name    = models.CharField(max_length=50)
    college_slug    = models.SlugField()
    college_email   = models.EmailField()
    college_country = models.CharField(max_length=50)
    college_phone   = models.CharField(max_length=13)
    college_contact = models.CharField(max_length=50)
    college_status  = models.CharField(max_length=50, choices=[("active","Active"),("inactive","Inactive")],default="active")

    
    def __str__(self):
        return self.college_name
    

class CollegeMedia(models.Model):
    image = models.ImageField(upload_to='college_images')
    
    def __str__(self):
        return self.image.name
    

class CollegeInfo(models.Model):
    college = models.OneToOneField(College, on_delete=models.DO_NOTHING, related_name='info')
    college_address               = models.CharField(max_length=200)
    college_fee_total             = models.IntegerField()
    college_course_offered        = models.CharField(max_length=200)
    college_required_twelth_marks = models.FloatField()
    college_exam_accepted         = models.CharField(max_length=100)
    college_scholarship           = models.PositiveIntegerField()
    college_course_duration       = models.PositiveIntegerField()
    college_media                 = models.ManyToManyField(CollegeMedia, blank=True, related_name='colleges')
    college_description           = models.TextField()
    college_intake_session        = models.CharField(max_length=30)
    college_yt_video              = models.URLField()

    def delete(self,*args,**kwargs):
        self.college.college_status= 'inactive'
        self.college.save()


    def __str__(self):
        return self.college.college_name