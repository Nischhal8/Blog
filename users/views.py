from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!! Now You are able to login !')
            return redirect('login')
                       
    else:
        form = UserRegisterForm()
    return render(request,'users/user_registration.html',{'form':form})

@login_required
def user_profile(request):
    if request.method == 'POST':
        import pdb; pdb.set_trace()
        user_form = UserUpdateForm(request.POST,instance = request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,
                                   instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        
            messages.success(request, f'Your account has been Updated!! ')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance= request.user.profile)
    
    context={
        'u_form':user_form,
        'p_form':profile_form
    }
    return render(request, 'users/profile.html',context)