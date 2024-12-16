from django.db import models
from django.contrib.auth.models import User

class Recurso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    disponivel = models.BooleanField(max_length=10, default=True)
    created_ad = models.DateField(auto_now_add=True)
    updated_ad = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
        
class Reserva(models.Model):
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    class Meta:
        permissions = [
            ("can_add_reserva", "Can add reserva"),
            ("can_delete_reserva", "Can delete reserva"),
            ("can_change_reserva", "Can change reserva"),
            ("can_view_reserva", "Can view reserva"),
        ]

    def __str__(self):
         return f"{self.recurso.nome} - {self.usuario.username}"