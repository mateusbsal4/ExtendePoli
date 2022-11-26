from django.contrib import admin

from .models import Equipe, Evento, Foto, Membro, Interessado
# Register your models here.

admin.site.register(Equipe)
admin.site.register(Evento)
admin.site.register(Foto)
admin.site.register(Membro)
admin.site.register(Interessado)