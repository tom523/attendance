from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Student(models.Model):
    name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CurrentWeek(models.Model):
    week_name = models.CharField(max_length=100)

    def __str__(self):
        return self.week_name


class AttendTime(models.Model):
    attend_time_name = models.CharField(max_length=100)

    def __str__(self):
        return self.attend_time_name


class AttendDay(models.Model):
    attend_day_name = models.CharField(max_length=100)

    def __str__(self):
        return self.attend_day_name


class Attend(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # 第几周
    week = models.ForeignKey(CurrentWeek, on_delete=models.CASCADE)
    # 星期几
    attend_day = models.ForeignKey(AttendDay, on_delete=models.CASCADE)
    # 具体时间段
    attend_time = models.ForeignKey(AttendTime, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name + self.week.week_name + \
               self.attend_day.attend_day_name + self.attend_time.attend_time_name













