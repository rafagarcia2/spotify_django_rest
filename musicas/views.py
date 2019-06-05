from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .serializers import MusicaSerializer, PlaylistSerializer
from .models import Musica, Playlist


class MusicaViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita todas as Músicas.
    """
    queryset = Musica.objects.all().order_by('-titulo')
    serializer_class = MusicaSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita as playlist.
    """
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
    search_fields = ('titulo',)


@api_view(['GET'])
def add_music(request, id_playlist, id_music):
    '''
    Adiciona uma música a playlist informada.
    '''
    playlist = get_object_or_404(Playlist, pk=id_playlist)
    musica = get_object_or_404(Musica, pk=id_music)

    playlist.musicas.add(musica)

    playlist.save()

    serializer = PlaylistSerializer(playlist)
    return Response(serializer.data)


@api_view(['GET'])
def lista_musicas_da_playlist(request, id_playlist):
    '''
    Lista todas as musicas de uma playlist.
    '''
    playlist = get_object_or_404(Playlist, pk=id_playlist)
    
    musicas = playlist.musicas.all()

    serializer = MusicaSerializer(musicas, many=True)
    return Response(serializer.data)
