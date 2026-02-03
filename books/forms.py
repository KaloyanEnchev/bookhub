from typing import Any

from django import forms

from books.models import Book, Tag


class BookFormBasic(forms.ModelForm):
    # tags = forms.CheckboxSelectMultiple()
    #
    # field_order = [
    #     'title',
    #     'pages',
    #     'price',
    # ]

    class Meta:
        exclude = ['slug',]
        model = Book

    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     super().__init__(*args, **kwargs)
    #     self.fields['tags'].queryset = Tag.objects.all()

class BookCreateForm(BookFormBasic):
    ...

class BookEditForm(BookFormBasic):
    ...

class BookDeleteForm(BookFormBasic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
        # widgets = {
        #     'all_fields': forms.TextInput(
        #         attrs={'disabled': True}
        #     )
        # }


class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )