from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserType, Course

class CustomUserAdmin(UserAdmin):
    model = UserType
    list_display = ('username','email','is_staff', 'is_active','is_client','is_trainer')
    search_fields = ('username', 'email')

    class Meta:
        verbose_name_plura='Users'


admin.site.register(UserType,CustomUserAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','desc','start_date_time','end_date_time')

    class Meta:
        verbose_name_plura='Courses'


admin.site.register(Course,CourseAdmin)
