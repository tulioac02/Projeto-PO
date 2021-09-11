from django.http import HttpResponse, JsonResponse, HttpRequest #return data response to the page
from django.shortcuts import render, redirect #render = html + django
from .models import Cliente,Cidade,Funcionario,Rota
from .models import ClienteForm,CidadeForm,FuncionarioForm,RotaForm
from . import solver

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

# Create your views here.
def main(request):
    return(render(request,'app/templates/base.html'))

def CadastroCliente(request):
    instance_form = ClienteForm()

    if(request.method == 'POST'):
        instance_form = ClienteForm(request.POST); #Case sending information to DB, defines form as POST
        instance_form.save();

    ClientesList = []
    Clientes = Cliente.objects.all() #Get all object in the DB and stores in a array to list in the html page
    for cli in Clientes:
        ClientesList.append(cli)

    return(render(request,'app/templates/CadastroCliente.html',{'form':instance_form,'Clientes':ClientesList})) #Go to the client Page

def CadastroCidade(request):
    instance_form = CidadeForm()

    if(request.method == 'POST'):
        instance_form = CidadeForm(request.POST); #Case sending information to DB, defines form as POST
        instance_form.save();

    CidadesList = []
    Cidades = Cidade.objects.all() #Get all object in the DB and stores in a array to list in the html page
    for cit in Cidades:
        CidadesList.append(cit)

    return(render(request,'app/templates/CadastroCidade.html',{'form':instance_form,'Cidades':CidadesList}))

def CadastroFuncionario(request):
    instance_form = FuncionarioForm()

    if(request.method == 'POST'):
        instance_form = FuncionarioForm(request.POST); #Case sending information to DB, defines form as POST
        instance_form.save();

    FuncionariosList = []
    Funcionarios = Funcionario.objects.all() #Get all object in the DB and stores in a array to list in the html page
    for func in Funcionarios:
        FuncionariosList.append(func)

    return(render(request,'app/templates/CadastroFuncionario.html',{'form':instance_form,'Funcionarios':FuncionariosList}))

def call_msg(b):
  return "Adicionar" if not b else "Remover"

#origem = str(Cidade.objects.get(name="Teste").latitude) +'%2C'+ str(Cidade.objects.get(name="Teste").longitude) #Lat,Long from diamantina as origin point
origin = {"id" : 0, "name" : "Diamantina", "cidade" : "Diamantina", "latitude" : -18.2381, "longitude" : -43.611, "using" : True}
destinos = [Struct(**origin)]
id = 1
for client in Cliente.objects.all():
  client.using = True
  client.msg = call_msg(True)
  client.id = id
  id = id+1
  destinos.append(client)

import requests #Make requests to external urls
import json
def CalcularRota(request):

    result = None #holds the final matrix

    if(request.method == 'POST'): #Calcular rota clicked
        string_api= "http://www.mapquestapi.com/directions/v2/routematrix?key=gAQQ0DBuAZAjvg02l6sU4N7cWBvNuW7o&ambiguities=ignore&doReverseGeocode=false&outFormat=json&routeType=fastest&unit=k&allToAll=true&manyToOne=false&from=-18.2381,-43.611" #FROM DIAMANTINA    
        xs = list(filter(lambda x : x.using, destinos))
        print(len(xs[1 : len(xs)]))
        if (len(xs[1 : len(xs)]) == 0) :
          return(redirect('Rota'));
        for dest in xs[1 : len(xs)]:
            string_api += "&to="+str(dest.latitude)+","+str(dest.longitude) #Get all the lat/long from the clients adress and combine in the url
        result = requests.get(string_api) #Get the json with the distance matrix (result.content)
        json_result = json.loads(result.content)
        result = solver.solve_model(solver.create_data_model(json_result['distance']))
        result = [(xs[i[0]], i[1]) for i in result[0]]

    instance_form = RotaForm()
    Clientes_obj = Cliente.objects.all();
    return(render(request,'app/templates/CalcularRota.html',{'form':instance_form,'Clientes':Clientes_obj,'Destinos':destinos[1 : len(destinos)],'Result':result}))

def AdicionarDestino(request,id):
    destino = destinos[id]
    destino.using = not destino.using
    destino.msg = call_msg(destino.using)

    return(redirect('Rota'));


#API to return a matrix of distances between coordinates, will be used in the gurobi or like tool 
#https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key=AIzaSyCA9cWof-bJvsqWfarRG5VMkJ5akQR_m70
