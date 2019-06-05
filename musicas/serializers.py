from rest_framework import serializers
from .models import Musica, Playlist


class MusicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musica
        fields = ('pk', 'titulo', 'cantor', 'ano_lancamento')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ('pk', 'titulo', 'usuario', 'ativo', 'data_criacao')