from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import banco_quest2


def questionario2(request):
    # Se a requisição for GET, mostra o formulário vazio
    if request.method == "GET":
        return render(request, 'questionario2.html')

    # Se a requisição for POST, processa os dados do formulário
    elif request.method == "POST":
        # Obtém todos os dados do formulário
        id = request.POST.get('id')
        altura = request.POST.get('altura')
        cintura = request.POST.get('cintura')
        peso = request.POST.get('peso')
        imc = request.POST.get('imc')
        pressao = request.POST.get('pressao')
        oximetria = request.POST.get('oximetria')
        frequencia_card = request.POST.get('frequencia_card')

        # Verifica se o ID foi enviado
        if id is not None:
            # Cria um novo objeto com os dados do formulário
            quest2_envio = banco_quest2(
                id=id, 
                altura=altura, 
                cintura=cintura, 
                peso=peso, 
                imc=imc,
                pressao=pressao, 
                oximetria=oximetria, 
                frequencia_card=frequencia_card
            )
            # Salva o objeto no banco de dados
            quest2_envio.save()

        # Redireciona para o questionário 3, passando o ID
        return render(request, 'questionario3.html', {"id": id})