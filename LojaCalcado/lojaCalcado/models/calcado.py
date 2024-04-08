from lojaCalcado.models import *

class Calcado(models.Model):
    descricao = models.CharField(null=False, max_length=100)
    tipo = models.ForeignKey(tipoCalcado, null=True, related_name='tipo', on_delete=models.SET_NULL)
    numero = models.DecimalField(max_digits=2, decimal_places=0)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.descricao}"