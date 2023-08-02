from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Department, Course


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    dob = forms.DateField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')])
    age = forms.IntegerField()
    number = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ChoiceField(choices=['Engineering', 'Medical', 'Commerce', 'Arts'])
    courses = forms.ChoiceField(choices=['BA', 'MA', 'Bcom', 'MBA', ''])
    purpose = forms.ChoiceField(choices=[('enquiry', 'Enquiry'), ('order', 'Order'), ('return', 'Return')])
    materials_provided = forms.MultipleChoiceField(choices=[('notebook', 'Notebook'), ('pen', 'Pen'), ('question_paper', 'Question Paper')],
                                                   widget=forms.CheckboxSelectMultiple)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']