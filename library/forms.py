from django.forms import ModelForm, Textarea

from .models import Book, Writer

# class BookForm(object):
#     """docstring for BookForm."""
#     class Meta:
#         model = Book


class WriterForm(ModelForm):
    """docstring for WriterForm."""
    class Meta:
        model = Writer
        fields = ['name','bio']
        widgets = {
            'bio': Textarea(attrs={'cols':60,'rows':40})
        }
