from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, CurrentWeek, Attend
from django.template import loader

# Create your views here.

def index(request):
    current_week = CurrentWeek.objects.all()[0].week_name
    monday12_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期一',
                                           attend_time__attend_time_name='上午12节')
    monday34_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期一',
                                           attend_time__attend_time_name='上午34节')
    monday_noon_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期一',
                                           attend_time__attend_time_name='中午')
    monday56_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期一',
                                           attend_time__attend_time_name='下午56节')
    monday78_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期一',
                                           attend_time__attend_time_name='下午78节')
    monday_night7to9_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期一',
                                           attend_time__attend_time_name='晚上7点到9点')

    tuesday12_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期二',
                                           attend_time__attend_time_name='上午12节')
    tuesday34_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期二',
                                           attend_time__attend_time_name='上午34节')
    tuesday_noon_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期二',
                                           attend_time__attend_time_name='中午')
    tuesday56_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期二',
                                           attend_time__attend_time_name='下午56节')
    tuesday78_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期二',
                                           attend_time__attend_time_name='下午78节')
    tuesday_night7to9_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期二',
                                           attend_time__attend_time_name='晚上7点到9点')

    wednesday12_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期三',
                                           attend_time__attend_time_name='上午12节')
    wednesday34_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期三',
                                           attend_time__attend_time_name='上午34节')
    wednesday_noon_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期三',
                                           attend_time__attend_time_name='中午')
    wednesday56_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期三',
                                           attend_time__attend_time_name='下午56节')
    wednesday78_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期三',
                                           attend_time__attend_time_name='下午78节')
    wednesday_night7to9_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期三',
                                           attend_time__attend_time_name='晚上7点到9点')

    thursday12_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期四',
                                           attend_time__attend_time_name='上午12节')
    thursday34_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期四',
                                           attend_time__attend_time_name='上午34节')
    thursday_noon_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期四',
                                           attend_time__attend_time_name='中午')
    thursday56_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期四',
                                           attend_time__attend_time_name='下午56节')
    thursday78_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期四',
                                           attend_time__attend_time_name='下午78节')
    thursday_night7to9_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期四',
                                           attend_time__attend_time_name='晚上7点到9点')

    friday12_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期五',
                                           attend_time__attend_time_name='上午12节')
    friday34_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期五',
                                           attend_time__attend_time_name='上午34节')
    friday_noon_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期五',
                                           attend_time__attend_time_name='中午')
    friday56_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期五',
                                           attend_time__attend_time_name='下午56节')
    friday78_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期五',
                                           attend_time__attend_time_name='下午78节')
    friday_night7to9_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期五',
                                           attend_time__attend_time_name='晚上7点到9点')


    saturday12_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期六',
                                           attend_time__attend_time_name='上午12节')
    saturday34_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期六',
                                           attend_time__attend_time_name='上午34节')
    saturday_noon_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期六',
                                           attend_time__attend_time_name='中午')
    saturday56_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期六',
                                           attend_time__attend_time_name='下午56节')
    saturday78_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期六',
                                           attend_time__attend_time_name='下午78节')
    saturday_night7to9_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期六',
                                           attend_time__attend_time_name='晚上7点到9点')

    sunday12_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期日',
                                           attend_time__attend_time_name='上午12节')
    sunday34_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期日',
                                           attend_time__attend_time_name='上午34节')
    sunday_noon_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期日',
                                           attend_time__attend_time_name='中午')
    sunday56_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期日',
                                           attend_time__attend_time_name='下午56节')
    sunday78_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期日',
                                           attend_time__attend_time_name='下午78节')
    sunday_night7to9_queryset = Attend.objects.filter(week__week_name=current_week, attend_day__attend_day_name='星期日',
                                           attend_time__attend_time_name='晚上7点到9点')

    day12_list = [monday12_queryset, tuesday12_queryset, wednesday12_queryset, thursday12_queryset,
                  friday12_queryset, saturday12_queryset, sunday12_queryset]
    day34_list = [monday34_queryset, tuesday34_queryset, wednesday34_queryset, thursday34_queryset,
                  friday34_queryset, saturday34_queryset, sunday34_queryset]
    day_noon_list = [monday_noon_queryset, tuesday_noon_queryset, wednesday_noon_queryset, thursday_noon_queryset,
                  friday_noon_queryset, saturday_noon_queryset, sunday_noon_queryset]
    day56_list = [monday56_queryset, tuesday56_queryset, wednesday56_queryset, thursday56_queryset,
                  friday56_queryset, saturday56_queryset, sunday56_queryset]
    day78_list = [monday78_queryset, tuesday78_queryset, wednesday78_queryset, thursday78_queryset,
                  friday78_queryset, saturday78_queryset, sunday78_queryset]
    day_night7to9_list = [monday_night7to9_queryset, tuesday_night7to9_queryset, wednesday_night7to9_queryset, thursday_night7to9_queryset,
                  friday_night7to9_queryset, saturday_night7to9_queryset, sunday_night7to9_queryset]


    # 统计每个学生的出勤时长
    attend_duration = {}
    student_queryset = Student.objects.all()
    for student in student_queryset:
        attend_queryset_each_student = Attend.objects.filter(student=student)
        hours = 0
        for attend in attend_queryset_each_student:
            # 取出晚上7点到9点的记录
            if attend.attend_time.attend_time_name == '晚上7点到9点':
                hours += 2
            else:
                hours += 1.5
        attend_duration[student.name] = hours
    sorted_attend_duration = sorted(attend_duration.items(), key=lambda item: item[1], reverse=True)
    template = loader.get_template('attend/index.html')
    context = {
        'day12_list': day12_list,
        'day34_list': day34_list,
        'day_noon_list': day_noon_list,
        'day56_list': day56_list,
        'day78_list': day78_list,
        'day_night7to9_list': day_night7to9_list,
        'sorted_attend_duration': sorted_attend_duration,
    }
    return HttpResponse(template.render(context, request))











