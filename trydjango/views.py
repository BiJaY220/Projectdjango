
#from django import Http
import random
from django.http import HttpResponse
from student.models import Student
from django.template.loader import render_to_string

def home_view(request,id =None , *args, **kwargs  ): 
    """
    take in request and provide a response 
    returns HTML as a response
    """
   
    number = random.randint(1, 6)
    # from database
    obj = Student.objects.get(id=number)
    #django template
    #my_list = Student.objects.all()
    student_queryset = Student.objects.all()

    context ={
        "query_set"  : student_queryset,
        "object": obj,
        "name": obj.name,
        "course": obj.course,
       # "context": obj.context

    }
    #rendering a template
    hel_STRING = render_to_string("home_view.html", context=context)
    
   

    return HttpResponse(hel_STRING)
    