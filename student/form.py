from django import forms
from django.shortcuts import render
from .models import Student



class StudentForm(forms.ModelForm):
      
    class Meta:

        model = Student
        fields = [
            'name',
            'course',
        ]


    def cleaned(self):
        data = self.cleaned_data
        print(data)
        name = data.get("name")
        qs = Student.objects.filter(name__iexact=name)
        if qs.exists():
            self.add_error("name", f"This name {name} has already been used. Please try again.")

        

        #name = cleaned_name.capitalize()

        return data
        




class StudentFormOld(forms.Form):
    
    name = forms.CharField()
    course = forms.CharField()


def cleaned_name(self):
    cleaned_name = self.cleaned_data.get("name")
    

    #name = cleaned_name.capitalize()

    return 



        
    
    