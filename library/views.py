from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Writer
# Create your views here.
# EQUIVALE A

class IndexView(generic.ListView):
    model = Writer

    #<nombre_app>/<nombre_modelo>_<list>.html
    #template_name = 'writers/writers.html'

class DetailView(generic.DetailView):
    model = Writer
    template_name = 'writers/writer.html'

def index(request):
    return HttpResponse(loader.get_template('writers/index.html').render({},request))


# def writers(request):
#     writers = Writer.objects.all()
#     context = {
#         'writer_list': writers,
#     }
#     return render(request,'writers/writers.html',context)
#
#
# def writer(request, writer_id):
#     #writ = Writer.objects.get(pk=writer_id)
#     writ = get_object_or_404(Writer,pk=writer_id)
#
#     return render(request,'writers/writer.html',{'writer':writ})

def writerEdit(request,writer_id=False):
    if(not writer_id):
        return render(request,'writers/form.html',{'writer':{id:''}})
    else:
        writer = get_object_or_404(Writer,pk=writer_id)
        return render(request,'writers/editar.html',{'writer':writer})

def saveWriter(request,writer_id=False):
    lista = request.POST
    if(not writer_id):
        writer = Writer()
    else:
        writer = get_object_or_404(Writer,pk=writer_id)

    writer.bio = lista.get('bio','biografia por defecto')
    writer.name = lista.get('nombre','Anonimo')
    writer.save() #insert or update
    return HttpResponseRedirect(reverse('detalle_escritor',args=(writer.id,)))

#Solo para pruebas inutilizados
# def hola(request,name):
#     return HttpResponse('hola '+name)
#
# def fullHola(request,name, age):
#     return HttpResponse('Hola '+name+' tienes '+str(age)+' de edad')
#
# def search(request):
#     parametro = request.GET.get('q',None)
#     return HttpResponse('usted busco {}'.format(parametro))
