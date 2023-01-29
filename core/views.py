from django.shortcuts import render
from .models import Information,Contact,Teacher,CourseList
# Create your views here.

def index(request):
    courses = Information.objects.all()
    return render(request, 'index.html', {'courses': courses})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        quary = request.POST.get('quary', '')

        contact = Contact(name=name,email=email,phone=phone,state=state,country=country,quary=quary)
        contact.save()
    return render(request, 'contact.html')

def getstarted(request):
    return render(request, 'getstarted.html')

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers':teachers})

def courses(request):
    courseList = CourseList.objects.all()
    return render(request, 'courses.html', {'courseList':courseList})