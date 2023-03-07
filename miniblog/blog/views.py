from django.shortcuts import render, HttpResponseRedirect,redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import Group
# Create your views here.
#Home page
def Home(request):
    posts=Post.objects.all()

    return render(request, 'blog/home.html',{'posts':posts})

#About page
def About(request):
    return render(request,'blog/about.html')

#Contact page
def Contact(request):
    return render(request,'blog/contact.html')

#dashbord page
def dashboard(request):
    if request.user.is_authenticated:
     posts=Post.objects.all()
     return render(request,'blog/dashboard.html',{'posts':posts})
    else:
       return redirect('/login')

#sigup page
def sigup(request):
    if request.method== 'POST':
     form=SignUpForm(request.POST)
     if form.is_valid():
        messages.success(request,"Sign Up Successfully!!")

        user=form.save()
        group=Group.objects.get(name="Authors")
        user.groups.add(group)

    else:
        form=SignUpForm()
    return render(request,'blog/sigup.html',{'form':form})


             
    


#login page
def User_login(request):
   if not request.user.is_authenticated:
    if request.method =="POST":
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            Username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user= authenticate(request, username=Username,password=password)
            if user is not None:
             login(request, user)
             messages.success(request,'Logged in Successfully')
             return HttpResponseRedirect('dashboard')
    else:
         form=LoginForm()
    return render(request, 'blog/login.html',{'form':form})
   else:
    return HttpResponseRedirect('dashboard')
          
    

#logout 
def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    




# Add Post
def Add_post(request):
      if request.user.is_authenticated:
        if request.method =="POST":
           form=PostForm(request.POST)
           if form.is_valid():
              title=form.cleaned_data['title']
              desc=form.cleaned_data['desc']
              pst=Post(title=title, desc=desc)
              pst.save()
              form=PostForm()
        else:      
           form=PostForm()

        return render(request,'blog/Add_post.html',{'form':form})
      else:
         return redirect('login')
      
# Update Post 
def Update_post(request,id):
      if request.user.is_authenticated:
        if request.method =="POST":
           pi=Post.objects.get(pk=id)
           form=PostForm(request.POST,instance=pi)
           if form.is_valid():
              form.save()
        else:
         pi=Post.objects.get(pk=id)
         form=PostForm(instance=pi)
        return render(request,'blog/Updatepost.html',{'form':form})
      else:
         return redirect('login')
      
# Delate post
def delate_post(request,id):
      if request.user.is_authenticated:
        if request.method =='POST':
           pi=Post.objects.get(pk=id)
           pi.delete()
        return HttpResponseRedirect('/dashboard')
      else:
         return redirect('login')