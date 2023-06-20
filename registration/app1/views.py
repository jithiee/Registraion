from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth.models import User 


# Create your views here.
def Homepage(request):
    return render(request,'home.html')


def Loginpage(request):
    return render(request,'login.html')


def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('Password')
        pass2 = request.POST.get('conformPassword')
        
        # print(uname,email,pass1)
        
        my_user =User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')

        
    return render(request,'signup.html')
    