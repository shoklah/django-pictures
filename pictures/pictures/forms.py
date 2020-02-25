from django import forms
from .models import *

class PictureForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), required=False)


    def __init__(self, user_id, *args, **kwargs):
        self.user_id = user_id
        user_id = kwargs.pop('user_id', None)
        super(PictureForm, self).__init__(*args, **kwargs)

        if self.user_id:
            self.fields['album'].queryset = Album.objects.filter(user_id=self.user_id)


    class Meta:
        model = Picture
        fields = ['title', 'image']


    def save(self, commit=True):
        return super(PictureForm, self).save(commit=commit)


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'cover']