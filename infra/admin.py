'''from django.contrib import admin
from .models import Processo

# Register your models here.
admin.site.register(Processo)'''

from django.contrib import admin
from .models import Processo, Documento

class DocumentoAdmin(admin.StackedInline):
    model = Documento

@admin.register(Processo)
class CaseAdmin(admin.ModelAdmin):
    inlines = [DocumentoAdmin]

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    pass