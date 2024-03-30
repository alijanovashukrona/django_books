from django.shortcuts import render,redirect

from .models import *
def home(request):
    if request.method=='POST':
        Kitob.objects.create(
            nom=request.POST.get('bookName'),
            narx =request.POST.get('bookPrice'),
            rasm=request.FILES.get('bookImage')
        )
        return redirect('/')
    data={
        'kitoblar':Kitob.objects.all()
    }
    return render(request,'book_records.html',data)

# def kitob_ochir(request,pk):
#
#     return redirect('/')


