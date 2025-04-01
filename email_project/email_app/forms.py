from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField(label='Email получателя')
    subject = forms.CharField(label='Тема', max_length=255)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)