from django import forms

from .models import *

from django.forms import ModelForm

from django.forms import BaseFormSet, BaseModelFormSet

# forms.py

# ...


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'content', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': '.form-select',
            }),

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-label': '.form-control',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'With textarea',
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'With textarea',
            }),

            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'customFile',
            }),
            
        }


# class NewItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ('name', 'description', 'content', 'image', 'category')

#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'aria-label': '.form-control',
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'aria-label': 'With textarea',
#             }),
#             'content': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'aria-label': 'With textarea',
#             }),
#             'image': forms.FileInput(attrs={
#                 'class': 'form-control',
#                 'id': 'customFile',
#             }),
#         }

#     def __init__(self, user, *args, **kwargs):
#         super(NewItemForm, self).__init__(*args, **kwargs)

#         # Restrict users to a single category
#         if not user.is_superuser:
#             allowed_category = Category.objects.get(name='Quotes')
#             self.fields['category'].queryset = Category.objects.filter(pk=allowed_category.pk)
#             self.fields['category'].initial = allowed_category
#             self.fields['category'].widget.attrs['disabled'] = 'disabled'
#         else:
#             self.fields['category'].widget = forms.Select(attrs={
#                 'class': 'form-select',
#                 'aria-label': '.form-select',
#             })




class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'content', 'image',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-label': '.form-control',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'With textarea',
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'With textarea',
            }),

            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'customFile',
            }),
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': 'Comment',
        }
        widgets = {
            'body': forms.TextInput(attrs={
                'class': 'form-control',
                'aria-label': 'form-control',
                'placeholder': 'Leave a Comment...',
                'autocomplete': 'off',
                
            }),
        }

        