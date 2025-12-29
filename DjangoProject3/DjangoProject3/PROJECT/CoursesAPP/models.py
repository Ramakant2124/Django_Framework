from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duration = models.IntegerField()
    course_fees = models.FloatField()

