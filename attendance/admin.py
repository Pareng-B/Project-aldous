from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time_in', 'time_out', 'total_hours')
    list_filter = ('date', 'user')
    search_fields = ('user__username',)

