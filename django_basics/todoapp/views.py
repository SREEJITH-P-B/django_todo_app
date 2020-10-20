from django.shortcuts import render,redirect
from .models import detailss

def home(request):
    return render(request,'todoapp/index.html')

def show(request):
        query_results = detailss.objects.all()
        context ={
            "results":query_results,
        }
        return render(request,'todoapp/show.html',context)

def details(request):
    if request.method=='POST':
        d=detailss()
        d.text=request.POST.get('text')

        d.completed=0
        d.save()
        return redirect('show')
def delete_item(request):
    query_results = detailss.objects.filter(completed=True).delete()
    return redirect('show')



def completed_item(request,ids):
    results=detailss.objects.get(pk=ids)
    if(results.completed==True):
            results.completed=False;
            results.save()
    else:
            results.completed=True;
            results.save()
    return redirect('show')
