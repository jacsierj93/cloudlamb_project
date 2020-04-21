from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.forms import modelform_factory

from .forms import WriterForm

from .models import Writer, Book
# Create your views here.
# EQUIVALE A

class IndexView(generic.ListView):
    model = Writer

class DetailView(generic.DetailView):
    model = Writer
    template_name = 'writers/writer.html'

def index(request):
    return HttpResponse(loader.get_template('writers/index.html').render({},request))


def writerEdit(request,writer_id=False):
    if(request.method == 'GET'):
        if(not writer_id):
            f = WriterForm()
            return render(request,'writers/form.html',{'form':f})
        else:
            writer = get_object_or_404(Writer,pk=writer_id)
            return render(request,'writers/editar.html',{'writer':writer})
    else:
        if(not writer_id):
            form = WriterForm(request.POST)
        else:
            w = get_object_or_404(Writer,pk=writer_id)
            form = WriterForm(request.POST,instance = w)

        writer = form.save()
        return HttpResponseRedirect(reverse('detalle_escritor',args=(writer.id,)))


class BookIndexView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

def manage_book(request):
    BookFormSet = modelform_factory(Book, fields=['year','title','resume','writer'])

    if request.method == 'GET':
        return render(request,'library/book_form.html',{'form':BookFormSet})
    else:
        formset = BookFormSet(request.POST)
        if(formset.is_valid()):
            book = formset.save()
        else:
            return HttpResponse('un elemento esta repetido')

        return HttpResponseRedirect(reverse('detail_book',args=(book.id,)))
