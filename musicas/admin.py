from django.contrib import admin
from .models import Musica, Playlist

class MusicaAdmin(admin.ModelAdmin):
	list_display = ['pk', 'titulo', 'cantor', 'ano_lancamento']
	search_fields = ['titulo', 'cantor']
	list_filter = ['titulo']


class PlaylistAdmin(admin.ModelAdmin):
	search_fields = ['titulo', 'usuario', 'data_criacao']
	list_filter = ['titulo', 'usuario']


admin.site.register(Musica, MusicaAdmin)
admin.site.register(Playlist, PlaylistAdmin)
