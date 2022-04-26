from django.db import models
from django.urls import reverse

class Student(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    courses = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    course = models.CharField(max_length=1, choices=courses, blank=True, default='1')

    group = models.CharField(max_length=6)

    def __str__(self):
        return '{0} {1} {2}'.format(self.surname, self.name, self.patronymic)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

class Supervisor(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)

    def __str__(self):
        return '{0} {1} {2}'.format(self.surname, self.name, self.patronymic)

class NIRS(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Student)
    supervisor = models.ForeignKey('Supervisor', on_delete=models.SET_NULL, null=True)
    date_of_start = models.DateField(null=True, blank=True)
    date_of_finish = models.DateField('Complete',null=True, blank=True)

    def authors_list(self):
        return [author.name for author in self.authors.all()]

    def __str__(self):
        return '{0}'.format(self.title)

    def get_absolute_url(self):
        return reverse('NIRS-detail', args=[str(self.id)])

class Article(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Student)
    supervisor = models.ForeignKey('Supervisor', on_delete=models.SET_NULL, null=True)
    ID = models.CharField(max_length=50)
    date_of_publication = models.DateField(null=True, blank=True)

    def authors_list(self):
        return [author.name for author in self.authors.all()]

    class Meta:
        ordering = ["date_of_publication"]
    
    def __str__(self):
        return self.title

class Competitions(models.Model):
    title = models.CharField(max_length=500)
    authors = models.ManyToManyField(Student)
    supervisors = models.ManyToManyField(Supervisor)
    place = models.CharField(max_length=200, default='СТИ НИЯУ "МИФИ"')
    date_of_the_event = models.DateField(null=True, blank=True)

    def authors_list(self):
        return [author.name for author in self.authors.all()]

    class Meta:
        ordering = ["date_of_the_event"]

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.date_of_the_event)

    def get_absolute_url(self):
        return reverse('comp-detail', args=[str(self.id)])

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    nirs = models.ForeignKey('NIRS', on_delete=models.SET_NULL, null=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)