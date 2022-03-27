from django.contrib import admin
from actors.models import *
from .models import *
# Register your models here.

#!FilmModelAdmin
class FilmModelAdmin(admin.ModelAdmin):
    #render_change_form function default admin panel
    def render_change_form(self,request,context,*args,**kwargs):
        context['adminform'].form.fields['actors'].queryset = Actor.objects.filter(is_star=True)
        return super().render_change_form(request,context,*args,**kwargs)
    
#!CommercialAdmin
class CommercialAdmin(admin.ModelAdmin):
    #render_change_form function default admin panel
    def render_change_form(self,request,context,*args,**kwargs):
        context['adminform'].form.fields['actors'].queryset = Actor.objects.filter(is_star=False)
        return super().render_change_form(request,context,*args,**kwargs)

admin.site.register(Film,FilmModelAdmin)#star actor list
admin.site.register(Commercial,CommercialAdmin)#commercial actor list well not start not popular not famous actor prominent actor

