from django.contrib import admin
from .models import Student


class adminStudent(admin.ModelAdmin):
    # the list only tells Django what to list on the admin site
    list_display = [
        "id",
        "registration_no",
        "first_name",
        "second_name"
    ]


admin.site.register(Student, adminStudent)

