from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import treasure
# Create your views here.
@login_required(login_url='login')

def HomePage(request):
    return render(request,'home.html')


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            #return HttpResponse("Your password and confrom password are not Same!!")
            #return render(request,{"Incorrect Password"})
            messages.error(request, 'Invalid credentials!')
            return redirect('signup')
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        if username=="admin@treasure.com":
            if pass1=="admin123":
                request.session['adm'] = 'adm'
                return redirect('/adm/')
        

        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            #print(user.email)
            login(request,user)
            request.session['email'] = user.email
            request.session['username'] = username
            
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")

    return render (request,'login.html')

def clue1Page(request):
    #context = {'timer': request.session.get('timer', 0)}
    if request.method=='POST':
        answer=request.POST.get('ans')
        print(answer)
        if(answer=='29'):
            messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            return redirect('clue2')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue1')
    return render(request,'clue1.html')
    
    

def clue2Page(request):
    if request.method=='POST':
        answer=request.POST.get('ans2')
        print(answer)
        if(answer=='Tomatoes'):
            messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            return redirect('clue3')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue2')
    return render(request,'clue2.html')


def clue3Page(request):
    if request.method=='POST':
        answer=request.POST.get('ans3')
        print(answer)
        if (answer=='18'):
            messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            return redirect('clue4')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue3')
    return render(request,'clue3.html')


def clue4Page(request):
    if request.method=='POST':
        answer=request.POST.get('ans4')
        print(answer)
        if (answer=='CBDEA'):
            messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            return redirect('clue5')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue4')
    return render(request,'clue4.html')

def clue5Page(request):
    if request.method=='POST':
        answer=request.POST.get('ans5')
        print(answer)
        if (answer=='Miss'):
            messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            return redirect('clue6')
        elif(answer=='Leave'):
            messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            return redirect('clue7')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue5')
    return render(request,'clue5.html')


def clue6Page(request):
    if request.method=='POST':
        answer=request.POST.get('ans6')
        print(answer)
        if(answer=='C'):
            messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            return redirect('clue8')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue6')
    return render(request,'clue6.html')
    


    
def clue7Page(request):
    email = request.session['email']
    username = request.session['username']
    print(email)
    print(username)
    if request.method=='POST':
        answer=request.POST.get('ans7')
        print(answer)
        if(answer=='81'):
            #messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            result=treasure(username=username, useremail=email, status="Incompleted")
            result.save()
            request.session.clear()
            return redirect('oops')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue7')
    return render(request,'clue7.html')

def clue8Page(request):
    email = request.session['email']
    username = request.session['username']
    print(email)
    print(username)
    if request.method=='POST':
        answer=request.POST.get('ans8')
        print(answer)
        if(answer=='11'):
            result=treasure(username=username, useremail=email, status="completed")
            result.save()
            request.session.clear()
            return redirect('winner')
        elif(answer=='26'):
            result=treasure(username=username, useremail=email, status="Incompleted")
            result.save()
            request.session.clear()
            messages.success(request,"Hurray! you got it, It's correct. The door opened and we got into another question. I guess we are getting closer to the tool")
            return redirect('clue9')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue8')
    return render(request,'clue8.html')


def clue9Page(request):
    if request.method=='POST':
        answer=request.POST.get('ans9')
        print(answer)
        if answer=='b':
            return redirect('oops')
        else:
            messages.warning(request, "Incorrect Answer")
            return redirect('clue9')
    return render(request,'clue9.html')

def indexPage(request):
    return render(request,'index.html')
def winnerPage(request):
    return render(request,'winner.html')

def oopsPage(request):
    return render(request,'oops.html')

def admPage(request):
    quiz_results = treasure.objects.all()
    context = {
        'quiz_results': quiz_results
    }
    return render(request, 'adm.html', context)
   