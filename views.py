from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import banco_quest2


def questionario2(request):
    if request.method == "GET":
        return render(request, 'questionario2.html')

    if request.method == "POST":
        id = request.POST.get('id')

        # ANTES: Várias variáveis individuais para cada campo do POST
        # DEPOIS: Acessamos diretamente request.POST.get() no create()
        if id is not None:
            # ANTES: Criação manual do objeto + save() separado
            # DEPOIS: Uso do objects.create() que já cria e salva em uma linha
             banco_quest2.objects.create(
                id=id,
                altura=request.POST.get('altura'),
                cintura=request.POST.get('cintura'),
                peso=request.POST.get('peso'),
                imc=request.POST.get('imc'),
                pressao=request.POST.get('pressao'),
                oximetria=request.POST.get('oximetria'),
                frequencia_card=request.POST.get('frequencia_card')
            )

        return render(request, 'questionario3.html', {"id": id})