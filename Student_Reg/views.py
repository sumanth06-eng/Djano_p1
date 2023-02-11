from django.shortcuts import render
from django.http import HttpResponse
from Student_Reg.models import Student_Details
from Student_Reg import forms
from Student_Reg.forms import Student_form


# Create your views here.
def home(Request):
    return render(Request,'Student_Reg/home.html')
# return HttpResponse("This is my home page")

def reg(Request):
    form=forms.Student_form()
    return render(Request, 'Student_Reg/reg.html',context=dict({'form_d':form}))

   # return HttpResponse("This is my Registration page")

def report(Request):
   std_details=Student_Details.objects.order_by('Std_ID')
   std_details_dict={'inserting_the_student_details':std_details}
   return render(Request, 'Student_Reg/Report.html', context=std_details_dict)






