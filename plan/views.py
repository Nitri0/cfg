# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
def registro(request):
    #ultimo_poll = Poll.objects.all().order_by('-pub_date')[:5]
    #toma un nombre de la plantilla como su primer argumento y un diccionario como su segundo argumento opcional. y devuelve un objeto django.http.HttpResponsecon una plantilla renderizada con el contexto dado.     
    return render_to_response('plan/PlanInversion.html')



def add_inversion(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/thanks/')