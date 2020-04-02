from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'placeholder': 'name@example.com'}))
    subject = forms.CharField(label="Objet du mail", required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)