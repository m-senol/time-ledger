from django.db import models
from django.conf import settings
from datetime import timedelta
from .constants import WORK_START_TIME, WORK_END_TIME

# Create your models here.

class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    late_duration = models.DurationField(default=timedelta(0))

    class Meta:
        unique_together = ('user', 'date')

    def calculate_work_duration(self):
        if self.check_in and self.check_out:
            check_in_time  = timedelta(hours=self.check_in.hour , minutes=self.check_in.minute)
            check_out_time = timedelta(hours=self.check_out.hour, minutes=self.check_out.minute)
            return max(check_out_time - check_in_time, timedelta(0))
        return timedelta(0)
    
    def calculate_late_duration(self):
        work_start_time = timedelta(hours=WORK_START_TIME.hour, minutes=WORK_START_TIME.minute)
        if self.check_in:
            check_in_time = timedelta(hours=self.check_in.hour, minutes=self.check_in.minute)
            return max(check_in_time - work_start_time, timedelta(0))
        return timedelta(0)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
