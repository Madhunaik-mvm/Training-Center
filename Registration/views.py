from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course,Batch,Student
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Prime Intuit Registration Page</h1>")
def Home(request):
    # return HttpResponse("<h1>Welcome to Prime Home  Page</h1>")
    # my_dict={'Insert_Me':"I am a text from Registration/Views.py now from sub templates","Insert_shivu":"Shivu is Just a escond inset point"}
    batch_list=Batch.objects.order_by('batch_ID')
    data_dict={'access_record':batch_list,'Insert_Me':"I am a text from Registration/Views.py now we do","Insert_shivu":"Shivu is Just a escond inset point"}
    #    batch_list = Batch.objects.raw('select * from Registration_Batch where start_date >"2021-06-01"')
    batch_list = Batch.objects.raw('select * from Registration_Batch')

    return render(request,'Registration/Index.html',context=data_dict)