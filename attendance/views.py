from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError

from .services import time_in, time_out
from .models import Attendance
from django.utils import timezone

@login_required
def dashboard(request):
    today = timezone.localdate()
    attendance = Attendance.objects.filter(
        user=request.user,
        date=today
    ).first()

    return render(request, 'attendance/dashboard.html', {
        'attendance': attendance
    })

@login_required
def time_in_view(request):
    try:
        time_in(request.user)
        messages.success(request, "Time in recorded successfully.")
    except ValidationError as e:
        messages.error(request, str(e))
    return redirect('attendance:dashboard')

@login_required
def time_out_view(request):
    try:
        time_out(request.user)
        messages.success(request, "Time out recorded successfully.")
    except ValidationError as e:
        messages.error(request, str(e))
    return redirect('attendance:dashboard')

