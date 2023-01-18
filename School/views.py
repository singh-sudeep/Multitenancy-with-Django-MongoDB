from django.shortcuts import render
from .models import Student


def get_students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'index.html', context)
