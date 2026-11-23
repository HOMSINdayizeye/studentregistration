from django import forms


class RegistrationForm(forms.Form):
    stude_name = forms.CharField(label='Student Name', max_length=100)
    student_email= forms.CharField( max_length=100, widget=forms.EmailInput())
    student_age = forms.IntegerField(label='Student Age', min_value=1, max_value=100)
    student_gender = forms.CharField(label='Student Gender', max_length=10)
    student_address = forms.CharField(label='Student Address', max_length=10, widget=forms.Textarea())
    student_marks = forms.IntegerField(label ='student marks ')
    