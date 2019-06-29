from django import forms

class CountForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "textarea",
            "placeholder": "Entre o seu texto aqui: "
        })
    )