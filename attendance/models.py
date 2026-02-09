from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)
    total_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['-date']

    def calculate_total_hours(self):
        if self.time_in and self.time_out:
            delta = self.time_out - self.time_in
            hours = delta.total_seconds() / 3600
            self.total_hours = round(hours, 2)

    def save(self, *args, **kwargs):
        self.calculate_total_hours()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

