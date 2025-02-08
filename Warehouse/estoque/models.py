from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Lote(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='lotes')
    numero_lote = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    data_entrada = models.DateField()
    data_validade = models.DateField()

    def __str__(self):
        return f"Lote {self.numero_lote} - {self.produto.nome}"