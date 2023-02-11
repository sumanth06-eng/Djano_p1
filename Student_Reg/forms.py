from django import forms
class Student_form(forms.Form):
    Std_ID = forms.IntegerField()
    name = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField
    phone = forms.IntegerField()
    email = forms.EmailField()