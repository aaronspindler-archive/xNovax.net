from django import forms


class ShortenURLForm(forms.Form):
    url = forms.URLField(label="Long URL", help_text="Enter a URL that you want to shorten!", widget=forms.TextInput(attrs={'placeholder': 'https://www.google.com'}))