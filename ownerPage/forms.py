from django import forms

from ownerPage.models import Owners


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Owners
        fields = ['notice','cpu','main_board','memory','graphic_card','ssd','mouse','keyboard']




