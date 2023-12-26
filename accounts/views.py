from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def login_views(request):
    if request.method == "POST":
        #print(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            user = form.get_user()
            
            login(request, user)
            return redirect('/')# this will redirect to home page after being logged in
    else:
        form = AuthenticationForm(request)
        context= {
        "form":form
        }
    return render(request, 'accounts/login.html',context)



def logout_views(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')
    
    return render(request, 'accounts/logout.html',context={})

def register_views(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    context ={"form":form}



    return render(request, 'accounts/register.html',context)
