from django.contrib import admin

# Register your models here.
from .models import NIRS, Competitions, Document, Student, Article, Supervisor

admin.site.register(NIRS)
admin.site.register(Competitions)
admin.site.register(Student)
admin.site.register(Article)
admin.site.register(Supervisor)
