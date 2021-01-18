
from django.shortcuts import render
from .models import seyvalue,seymaterial,Seytext
import numpy
import json

# Create your views here.


def toWelcome(request):
    return render(request, 'welcome.html')
def apitest(request):
    request_material = request.GET['material']
    print (request_material)
    selectedmaterial = seymaterial.objects.get(mname = request_material)
    print(selectedmaterial)
    seydata = Seytext.objects.get(textnum = selectedmaterial)
    print(seydata.content)
    list_1D = seydata.content.split()
    print(list_1D)
    list_row= int(len(list_1D)/4)
    list_4D = numpy.array(list_1D).reshape(list_row,4)
    print(list_4D)

    return render(request,'showdata.html',{'response': request_material,'table':seydata.content,'sey_list':json.dumps(list_4D.tolist())})


