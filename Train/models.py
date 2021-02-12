from django.db import models

# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length = 10)
    Platform_no = models.CharField(max_length = 10)

# class Train(models.Model):
#     name = models.CharField(max_length = 100)
#     Platform_no = models.IntegerField()
#     # Stops = models.IntegerField()
#     # Enter_Time = models.TimeField("12:00:00")
#     # Exit_Time = models.TimeField(auto_now=False, auto_now_add=False)
#     def __str__(self):
#         return name + '|' + str(Platform_no)
#                # + ' | ' + str(Enter_Time)
#                # + ' | ' + str(Exit_Time)