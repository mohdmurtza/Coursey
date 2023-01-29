from django.contrib import admin
from .models import Information,Contact,Teacher,CourseList
# Register your models here.

# register.site.admin(Information)
admin.site.register(Information)
admin.site.register(Contact)
admin.site.register(Teacher)
admin.site.register(CourseList)