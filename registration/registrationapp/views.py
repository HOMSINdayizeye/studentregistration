from django.http import request
from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            student_name =   form.cleaned_data['stude_name']
            student_email =  form.cleaned_data['student_email']
            student_age =    form.cleaned_data['student_age']
            student_gender=  form.cleaned_data['student_gender']
            student_address= form.cleaned_data['student_address']
            student_marks =  form.cleaned_data['student_marks'] 

            return render(request, 'views.html', {'student_name':'student_name'})
        else:
            context = {}
            context['form'] = RegistrationForm()  
            return render(request, 'views.html', context)

    return render(request, 'views.html', {'form': RegistrationForm()})

