from django.db import models


class Activity(models.Model):
    ACTIVITY_TYPE = (
        ('I', 'Indoor'),
        ('O', 'Outdoor'),
        ('S', 'Specialty')
    )
    activity_name = models.CharField(max_length=50)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPE)
    activity_pub_date = models.DateTimeField('Date Published')
    activity_owner = models.CharField(max_length=100)
    activity_status = models.CharField(max_length=10)
    activity_location = models.CharField(max_length=50)
    activity_pay = models.IntegerField()
    activity_comments = models.CharField(max_length=250)