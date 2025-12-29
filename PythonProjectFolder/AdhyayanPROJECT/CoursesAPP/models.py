from django.db import models

# Create your models here.
class CourseModel(models.Model):
    course_name = models.CharField(max_length=200)
    course_duration = models.FloatField()
    course_fees = models.FloatField()


    def __str__(self):
        return self.course_name