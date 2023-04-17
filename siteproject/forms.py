from .models import User, Music
from django.forms import ModelForm, TextInput, FileInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

        widgets = {
            "email": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),
            "username": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username"
            }),
            "password": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Password"
            }),

        }

class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist', 'publication_date', 'isbn', 'album', 'image', 'duration', 'audio_file']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title",

            }),
            "artist": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Artist"
            }),
            "publication_date": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Publication Date"
            }),
            "isbn": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Identical Number"
            }),
            "image": FileInput(attrs={
                "class": "form-control",
                "placeholder": "Image"
            }),
            "audio_file":  FileInput(attrs={
                "class": "form-control",
                "placeholder": "Audio"
            }),

            "album": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Album"
            }),

            "duration": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Duration"
            }),
        }
