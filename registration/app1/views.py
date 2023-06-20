from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import  authenticate , login


# Create your views here.

def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('Password')
        pass2 = request.POST.get('conformPassword')
        
        # print(uname,email,pass1)
        if pass1 != pass2:
            return HttpResponse("<h3>your passwords are not same</h3> <a href=''  >go backpage</a> ")
        else:
            my_user =User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

        
    return render(request,'signup.html')


# ============================================================================================


def Loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('Pass')
        # print(username,pass1)
        
        user=authenticate(request,username =username, Password =pass1)
        print(user)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or passward is incorrect...!!! ")
        
    return render(request,'login.html')



# ===================================================================================

def Homepage(request):
    return render(request,'home.html')
    