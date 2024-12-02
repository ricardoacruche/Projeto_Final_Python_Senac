from django.db import models 

class Candidato (models.Model):
    nome= models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome
    
    """No Django, o __str__ define como o objeto será representado como texto.
No caso do modelo Candidato, ele diz que, sempre que um objeto desse modelo for exibido como texto
(por exemplo, no painel administrativo do Django), o nome do candidato será mostrado e o deixa a representação mais amigável."""