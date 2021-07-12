from django.http import HttpResponse
from django.shortcuts import render , redirect
from .forms import UploadFileForm
from pdf2docx import parse
from pathlib import Path
import os
def handle_uploaded_file(f):
    with open('name.pdf', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    parse('name.pdf', 'name.docx')
    try:
        os.rename('name.docx','pdf2word/static/name.docx')
    except:
        os.remove('pdf2word/static/name.docx')
        os.rename('name.docx', 'pdf2word/static/name.docx')
def Index(request):

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        print('yessss12')
        if form.is_valid():
            print('valid')
            print('file',type(request.FILES['file']))
            handle_uploaded_file(request.FILES['file'])

        return render(request, 'pdf2word/download_page.html', {})
    else:
        print('shot')
        form = UploadFileForm()
        return render(request,'pdf2word/main_index.html',{'form':form,'sb':'submit','fd':'action-button'})