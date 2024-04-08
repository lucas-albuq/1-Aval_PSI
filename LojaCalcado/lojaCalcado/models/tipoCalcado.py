from lojaCalcado.models import *

class tipoCalcado(models.Model):
    descricao = models.CharField(null=False, max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descricao}"