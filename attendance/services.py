from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Attendance

def time_in(user):
    today = timezone.localdate()

    attendance, created = Attendance.objects.get_or_create(
        user=user,
        date=today
    )

    if attendance.time_in:
        raise ValidationError("Already timed in today.")

    attendance.time_in = timezone.now()
    attendance.save()
    return attendance

def time_out(user):
    today = timezone.localdate()

    try:
        attendance = Attendance.objects.get(user=user, date=today)
    except Attendance.DoesNotExist:
        raise ValidationError("No time-in record for today.")

    if attendance.time_out:
        raise ValidationError("Already timed out today.")

    attendance.time_out = timezone.now()
    attendance.save()
    return attendance

