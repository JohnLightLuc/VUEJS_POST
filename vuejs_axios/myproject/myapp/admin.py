from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Inscription)
class InscriptionAdmim(admin.ModelAdmin):
    list_display = ('nom', 'email', 'password', 'photo', 'statut', 'date_add', 'date_up')
    list_filter = ('statut','date_add', 'date_up')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    actions = ('active','desactive')

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request,"La selection a été desactivés avec succes")
    
    active.short_description = 'Activer'


    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request,"La selection a été desactivés avec succes")
    
    desactive.short_description = 'Desactiver'