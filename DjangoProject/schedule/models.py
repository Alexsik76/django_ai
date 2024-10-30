from django.db import models
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField


class Link(models.URLField):
    TYPE_CHOICES = {
        "TG": "Telegram",
        "GDRIVE": "Gdrive",
        "LOCAL": "local",
        "OTHER": "other",
    }
    link_type = models.CharField(max_length=8, choices=TYPE_CHOICES, default="other")
    icon_path = models.ImageField(blank=True)


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    tg_link = Link(blank=True)

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def __str__(self):
        return self.full_name



class AcademicDiscipline(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.CharField(max_length=1000, blank=True)
    link_desk = Link(blank=True)
    teacher = models.ForeignKey(Teacher, null=True, blank=True,  on_delete=CASCADE,  related_name='discipline')
    link_class = Link(blank=True)
    link_disk = Link(blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    TYPE_CHOICES = {
        "EXAM":         "exam",
        "EXAM_TEST":    "exam_test",  # залік
        "LAB":          "lab",
        "TEST":         "test",
        "COURSE_WORK":  "course_work"
    }
    task_type = models.CharField(max_length=11, choices=TYPE_CHOICES, default="lab")
    date = models.DateTimeField(blank=True)
    discipline = models.ForeignKey(AcademicDiscipline, on_delete=CASCADE, blank=True)
    link = Link(blank=True)
    score = models.IntegerField(blank=True, null=True)
    group = models.BooleanField(default=False, help_text="Can be performed by a group.")
    work_space = Link(blank=True)
    group_work_space = Link(blank=True)
