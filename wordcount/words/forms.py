from django import forms

class text(forms.Form):
    total_words = forms.CharField(widget=forms.Textarea)