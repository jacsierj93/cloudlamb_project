from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),

     path('escritores',views.IndexView.as_view(),name='ruta_escritores'),
     path('escritor/<int:pk>', views.DetailView.as_view(),name="detalle_escritor"),

    # path('escritores',views.writers,name='ruta_escritores'),
    #path('escritor/<int:writer_id>',views.writer,name="detalle_escritor"),

    path('nuevo',views.writerEdit,name="nuevo_escritor"),
    path('editar/<int:writer_id>',views.writerEdit,name="editar_escritor"),

    path('edit/<int:writer_id>',views.writerEdit,name="form_editar"),
    path('save',views.writerEdit,name="guardar"),

    path('books',views.BookIndexView.as_view(),name='list_books'),
    path('book/<pk>',views.BookDetailView.as_view(),name='detail_book'),

    path('book_insert',views.manage_book,name="book_form"),
    path('book_save',views.manage_book,name="book_save")


    # path('saludar/<str:name>',views.hola,name='hola'),
    #
    # path('saludar/<str:name>/edad/<int:age>',views.fullHola,name='ruta_saludar'),
    #
    # path('search',views.search,name='search'),

]
