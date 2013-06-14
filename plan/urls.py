from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from plan.models import Inversion
from plan.form import InversionForm
# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$',
         ListView.as_view(
            # queryset=Inversion.objects.order_by('-pub_date')[:10],
             model = Inversion,
             #context_processors = InversionForm(),
             context_object_name='Planes',
             template_name='plan/index.html'),
         name='plan'),

     url(r'^registro/$', 'plan.views.registro'),    
                
)


