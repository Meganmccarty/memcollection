from django import forms

class ContactForm(forms.Form):
    from_email = forms.CharField(required=True, label='Email')
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'form-control'}