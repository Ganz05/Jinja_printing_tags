from django.shortcuts import render

# Create your views here.
def new(request):
    data='succussfull'
    d={'login':data}
    return render(request,'login.html',context=d)


