from rest_framework import serializers
from .models import Musica, Playlist


class MusicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musica
        fields = ('pk', 'titulo', 'cantor', 'ano_lancamento')


class MusicaSimplesSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(source='titulo')

    class Meta:
         model = Musica
         fields = ('title', )


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    musics = MusicaSimplesSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ('pk', 'titulo', 'usuario', 'musics', 'ativo', 'data_criacao')
