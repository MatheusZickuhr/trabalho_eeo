import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.models import Pessoa

# get request
class HomeView(ListView):
    template_name = 'home.html'
    model = Pessoa


# post request
@csrf_exempt
def post(request):
    data = json.loads(request.body)
    pessoa_id = data['id']
    pessoa = Pessoa.objects.get(id=pessoa_id)
    pessoa_dict = {'nome': pessoa.nome, 'email': pessoa.email, 'idade': pessoa.idade}
    return JsonResponse({'pessoa': pessoa_dict}, safe=False)


# put request
@csrf_exempt
def put(request):
    data = json.loads(request.body)
    id = data['id']
    nome = data['nome']
    email = data['email']
    idade = data['idade']
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.email = email
    pessoa.save()
    pessoa_dict = {'nome': pessoa.nome, 'email': pessoa.email, 'idade': pessoa.idade}
    return JsonResponse({'pessoa': pessoa_dict}, safe=False)


# delete request
@csrf_exempt
def delete(request):
    data = json.loads(request.body)
    id = data['id']
    nome = data['nome']
    email = data['email']
    idade = data['idade']
    pessoa = Pessoa.objects.get(id=id)
    pessoa_dict = {'nome': pessoa.nome, 'email': pessoa.email, 'idade': pessoa.idade}
    return JsonResponse({'pessoa': pessoa_dict}, safe=False)
