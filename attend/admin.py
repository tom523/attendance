from django.contrib import admin
from .models import Question, Student, Attend, CurrentWeek, AttendTime, AttendDay

# Register your models here.
admin.site.register(Student)
admin.site.register(Attend)
admin.site.register(CurrentWeek)
admin.site.register(AttendTime)
admin.site.register(AttendDay)






