from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.real_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)

    def __str__(self):
        return "{} from {} to {}".format(self.user.real_name, self.start_time, self.end_time)
