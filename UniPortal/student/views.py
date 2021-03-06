from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import NIRS, Competitions, Student, Article, Document
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class NIRSListView(generic.ListView):
    model = NIRS
    paginate_by = 10

from django import forms

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)

@login_required
def NIRS_detail_view(request,pk):
    NIRS_id=get_object_or_404(NIRS, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.nirs = NIRS_id
            doc.save()
            return redirect('profile')
    else:
        form = DocumentForm()
    
    docs = []
    for doc in Document.objects.all():
        if doc.nirs == NIRS_id:
            docs.append(doc)
            
    return render(
        request,
        'student/NIRS_detail.html',
        context={
            'nirs':NIRS_id,
            'docs': docs[-4:],
            'form': form          
        }
    )
from django.http import FileResponse

def download(responce,pk):
    doc_id = get_object_or_404(Document, pk=pk)
    doc = open('static'+doc_id.document.url[7:], 'rb')
    responce =FileResponse(doc)
    return responce

class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 10

class CompListView(generic.ListView):
    model = Competitions
    paginate_by = 10

class CompDetailView(generic.DetailView):
    model = Competitions