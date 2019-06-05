from django.db import models

class Musica(models.Model):
    titulo = models.CharField('Título', max_length=100)
    cantor = models.CharField('Cantor', max_length=100)
    ano_lancamento = models.IntegerField('Ano Lançamento')
    
    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'
        ordering = ('titulo', 'cantor')


class Playlist(models.Model):
    titulo = models.CharField('Título', max_length=200)
    usuario = models.CharField('Usuário', max_length=200)
    musicas = models.ManyToManyField(Musica)

    ativo = models.BooleanField('Ativo', default=True)
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
        ordering = ('titulo', 'usuario')