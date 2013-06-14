'''
Created on 04/06/2013   
@author: edwin-ca
'''
from plan.models import Inversion, Linea_accion,Inversion_lineas_accion , Vocero, Inversion_vocero
from django.contrib import admin

class lineasAccionInLine(admin.TabularInline):
    model = Inversion_lineas_accion
    extra = 3
    max_num = 5
    
class VoceroInLine(admin.StackedInline):
    #fieldsets = ['nombre', 'apellido']
    model = Inversion_vocero
    #fields = ('nombre', )
    extra = 2
    max_num = 3
    
    
       
class PlanInversionAdmin(admin.ModelAdmin):
    list_display  = ['id','nombre', 'descripcion','codigo','pub_date'] #muestra campos individuales de la bd
    fieldsets = [
                 (None, {'fields': ['codigo']}),
                  ('Informacion', {
                                   'fields' : ['nombre','descripcion']}
                   ),
                  ]
    inlines = [VoceroInLine]
    inlines += [lineasAccionInLine]
    list_filter = ['descripcion']
    search_fields = ['codigo']
    
admin.site.register(Inversion,PlanInversionAdmin)

class LineaAccionAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','pub_date','activo']
    fieldsets = [
                 (None, {'fields': ['nombre']}),
                  ('Informacion', {
                                   'fields' : ['activo']}
                   ),
                  ]
    
    search_fields = ['nombre']
    list_filter = ['activo']

class VoceroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'correo_electronico', 'cedula_identidad']
    fieldsets = (
        (None, {
            'fields': ('nombre', 'apellido','correo_electronico', 'cedula_identidad')
        }),
    )

admin.site.register(Linea_accion,LineaAccionAdmin)
admin.site.register(Vocero,VoceroAdmin)