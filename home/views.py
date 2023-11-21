from django.shortcuts import render
from django.shortcuts import render
from django.urls import is_valid_path
from .form import *
from .models import *
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import get_user_model


def IndexView(request):
    useredit = UserModel.objects.all()
    ctx = {
            'useredit':useredit
        }
    return render(request, 'index.html', ctx)


def EditUserView(request,imgid):
    userimage_id = UserModel.objects.get(id=imgid)
    if request.method == "POST":
        form = EditImgForm(request.POST, request.FILES, instance=userimage_id)
        if form.is_valid():        
            form.save()
            return redirect('/')
        else:
            return redirect('edituser')
        

    form = EditImgForm(instance=userimage_id)
    userimage = UserModel.objects.filter(username_id=imgid)
    ctx ={
        'form':form,
        'userimage':userimage
    }

    return render(request, 'edituser.html',ctx)



def AddNFTView(request,addid):
    profile_id = UserModel.objects.get(id=addid)
    if request.method == "POST":
        form = AddNFTform(request.POST, request.FILES, instance=profile_id )
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            Highest_Bid= form.cleaned_data['Highest_Bid']
            image = form.cleaned_data['image']        
            profil_data = AddNftModel(name=name,price=price,image=image,Highest_Bid=Highest_Bid, user=profile_id )
            profil_data.save()
            return redirect('nft')

        else:
            print('error')
            return redirect('addnft')
        
    form = AddNFTform()
    nft = AddNftModel.objects.filter(user_id=addid)
    ctx ={
        'form':form,
        'nft':nft
    }
    
    return render(request, 'addnft.html',ctx)
    

def RegisterView(request):
    if  request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('login')
        else :
            messages.error(request, "Ma'lumotlaringizni noto'g'ri kiritdingiz!")
            return redirect('register')
    form = RegisterForm()
    ctx = {
            'form' : form
        }
    
    return render(request, 'register.html',ctx)

def LoginView(request):
    if request.POST:
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            user = authenticate(request,username=username, password=password1)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Ma'lumotlaringizni noto'g'ri kiritdingiz!")
        else:
            messages.error(request, "Parolingiz bir hil bo'lishi kerek!")
    form = LoginForm()
    ctx = {
        "form": form,
        
    }
    return render(request, 'login.html',ctx)
    
def LogoutView(request):
    logout(request)
    return redirect('login')



def RankingView(request):
    useredit = UserModel.objects.all()
    ctx = {
            'useredit':useredit
        }

    
    return render(request,'rankings.html',ctx)

def ConnectView(request):
    
    return render(request,'connect.html',{})


def MarketpaceView(request,):
    nft = AddNftModel.objects.all()
    useredit = UserModel.objects.all()
    ctx ={
        'nft':nft,
        'useredit':useredit
    }
    return render(request,'marketpace.html',ctx)

def NFTView(request):
    nft = AddNftModel.objects.all()
    useredit = UserModel.objects.all()
    ctx ={
        'nft':nft,
        'useredit':useredit
    }
    return render(request,'nft.html',ctx)

@login_required()
def EditNftProjectView(request,eddid):
    edit_project = AddNftModel.objects.get(id=eddid)
    if request.method=="POST":
        form = AddNFTform(request.POST, instance=edit_project)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('editnftprjc')
    form = AddNFTform(instance=edit_project)
    ctx={
        'form':form,
        'edit_project': eddid
    }
    return render(request,'editnftprjc.html',ctx)




@login_required()
def DeleteNfTView(request,delete_id):
    delete_project = AddNftModel.objects.get(id=delete_id)
    print(delete_project)
    if request.POST:
        delete_project.delete()
        return redirect('/')
    else:
        ctx={
            'delete_project':delete_project
        }

    return render(request,'delnft.html',ctx)