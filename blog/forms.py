from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "input",
            "placeholder": "Seu nome:"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "textarea",
            "rows": "4",
            "placeholder": "Entre seu comentário aqui:"
        })
    )