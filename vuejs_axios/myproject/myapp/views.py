from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Inscription

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    print('print = ', request.file('files') )
    # postdata = json.loads(request.body)
    # print(postdata)
    # name = postdata['name']
    # email = postdata['email']
    # password = postdata['password']
    
    succes = False
    # try:
    #     newperson = Inscription()
    #     newperson.name = name
    #     newperson.email = email
    #     newperson.password = password
    #     newperson.photo = myfile
    #     newperson.save()
    #     succes = True
    #     reponse = 'Vous avez été bien enregistré!'
    # except:
    #     succes = False
    #     reponse = "Probleme d'enregistrement !"
    datas = {
        'succes':succes,
        'reponse':'reponse',
        }
    return JsonResponse(datas, safe=False)