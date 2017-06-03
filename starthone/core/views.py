from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentForm

#main page for the image sessions got source from github but i modify the code for the assignment
def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })
#delete the images that i uploaded got source from github but i modify the code for the assignment
def delete_document(request,pk):
    try:
        Document.objects.get(id=pk).delete()
    except Document.DoesNotExist:
        pass
    return redirect('home')
def content(request):
    return render(request, 'core/content.html', {'section': 'about'})
@login_required
def crowdsourcing(request):
    if request.method == 'POST':
        return redirect('model_form_upload')
    return render(request, 'core/model_form_upload.html', {

    })
#def for the uploading the images got source from github but i modify the code for the assignment

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_form_upload')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
