from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Writer
# Create your views here.
# EQUIVALE A

class IndexView(generic.ListView):
    model = Writer

class DetailView(generic.DetailView):
    model = Writer
    template_name = 'writers/writer.html'

def index(request):
    return HttpResponse(loader.get_template('writers/index.html').render({},request))


# def writers(request):
#     writers = Writer.objects.all()
#     x = {
#         'writer_list': writers,
#         'usuario':'JACSIEL'
#     }
#
#     return render(request,'writers/writers.html',x)


# def writer(request, writer_id):
#     writ = get_object_or_404(Writer,pk=writer_id)
#     return render(request,'writers/writer.html',{'writer':writ})



def writerEdit(request,writer_id=False):
    if(request.method == 'GET'):
        if(not writer_id):
            return render(request,'writers/form.html',{})
        else:
            writer = get_object_or_404(Writer,pk=writer_id)
            return render(request,'writers/editar.html',{'writer':writer})
    else:

        if(not writer_id):
            writer = Writer()
        else:
            writer = get_object_or_404(Writer,pk=writer_id)

        lista = request.POST
        writer.bio = lista.get('bio','biografia por defecto')
        writer.name = lista.get('nombre','Anonimo')
        writer.save() #insert UPDATE
        return HttpResponseRedirect(reverse('detalle_escritor',args=(writer.id,)))
