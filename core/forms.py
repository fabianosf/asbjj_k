from django import forms



class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Seu Nome'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Seu Email'}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Sua Mensagem'}))
