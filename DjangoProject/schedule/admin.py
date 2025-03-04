from django.contrib import admin
from schedule.models import Teacher, AcademicDiscipline, Task

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["get_full_name", "disciplines"]

    def disciplines(self, obj):
        return ', '.join([a.name for a in obj.discipline.all()])

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            'discipline'
        )


@admin.register(AcademicDiscipline)
class AcademicDisciplineAdmin(admin.ModelAdmin):
    list_display = ["name", "descriptions", "teacher"]
    list_display_links = ["name", "teacher"]

class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)