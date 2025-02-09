from django.db import models

# Create your models here.

class Produto(models.Model):
    #Um produto tem um nome, lote, quantidade(soma dos lotes), preço, data de entrada e data de validade(por lote).
    nome = models.CharField(max_length=70)
    preço = models.DecimalField(max_digits=7, decimal_places=2)
    data_entrada = models.DateField()

    @property #Propriedade que retorna a quantidade total de produtos em um estoque.
    def quantidade(self):
        return sum([lote.quantidade for lote in self.lote_set.all()])
    def __str__(self):
        return self.nome
    
class Lote(models.Model):
    #Um lote tem uma quantidade, data de validade, um produto asociado a ele e um fornecedor.
    quantidade = models.IntegerField()
    data_validade = models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=70) #Tipo do produto (Ex: Alimento, Medicamento, etc.) e peresível/não peresível.
    #fornecedor = models.CharField(max_length=70) (Não implementado) (chave estrageira para um fornecedor)

    def __str__(self):
        return self.produto.nome + ' - ' + self.data_validade.strftime('%d/%m/%Y')