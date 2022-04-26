from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from student.models import NIRS, Competitions, Student, Article, Document
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    
    return render(
        request,
        'index.html',
    )

@login_required
def profile(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    for std in Student.objects.all():
        if std.name==request.user.first_name:
            stud = std
            break
        stud = None
    
    if stud != None:
        surname = stud.surname
        name = stud.name
        patronymic = stud.patronymic
        
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    user_articles = []
    for article in Article.objects.all():
        for x in article.authors_list():
            if stud.name in x:
                user_articles.append(article)
    
    user_nirs = []
    for nirs in NIRS.objects.all():
        for x in nirs.authors_list():
            if stud.name in x:
                user_nirs.append(nirs)

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'profile.html',
        context={
            'surname':surname,
            'name':name,
            'patronymic':patronymic,
            'num_visits':num_visits,
            'articles' :user_articles,
            'nirs': user_nirs
            }
    )