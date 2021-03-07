from django.shortcuts import render

def home(request):
    return render(request,'home.html',{'name':'Atik Salim rangnekar'})
# Create your views here.
def add(request):
    val1 = int(request.POST['name1'])
    val2 = int(request.POST['name2'])
    res = val1 + val2
    return render(request, "result.html",{'result': res})
