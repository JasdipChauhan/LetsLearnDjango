from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    output = ', '.join([str(courses) for courses in courses])
    return HttpResponse(output)

