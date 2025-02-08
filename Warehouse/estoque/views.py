from django.shortcuts import render, get_object_or_404
from .models import Produto
import models

# Create your views here.

def listar_produtos(request):
    produtos = Produto.objects.annotate(
        quantidade_total=models.Sum('lotes__quantidade')
    )
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    lotes = produto.lotes.all()  # Recupera todos os lotes do produto
    return render(request, 'produtos/detalhes.html', {'produto': produto, 'lotes': lotes})