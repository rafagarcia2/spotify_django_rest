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


@api_view(['POST'])
def add_music(request, id_playlist, id_musica):
    '''
    Adiciona uma música a playlist informada.
    '''
    playlist = get_object_or_404(Playlist, pk=id_playlist)
    musica = get_object_or_404(Musica, pk=id_musica)
    
    playlist.musicas.add(musica).save()

    serializer = PlaylistSerializer(playlist)
    return Response(serializer.data)