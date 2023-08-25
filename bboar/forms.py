from django.forms import ModelForm
from .models import Product, Rubric
from django import forms


class ProductForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control custom"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control custom"}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control custom"}))
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),widget=forms.Select(attrs={"class":"myfield"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"myfield"}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"myfield"}))
    addres = forms.CharField(widget=forms.Textarea(attrs={"class":"myfield"}))
    kind = forms.ChoiceField(choices=(('b','Куплю'),('s','Продам'),('c','Обменяю')),widget=forms.Select(attrs={"class":"myfield"}))
    class Meta:
        model = Product
        fields = ("title","content","price","rubric","email","phone_number","addres","kind")
