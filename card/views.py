from django.shortcuts import render,redirect,get_object_or_404
import datetime as dt
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.db.models.base import ObjectDoesNotExist
from .models import FlashCard
from .forms import SignUpForm,CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def welcome(request):
    
    return render(request, 'home.html')

def registerPage(request):
    
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login')
    else: 
        form=SignUpForm()
    
    return render(request, 'django_registration/registration_form.html', {'form':form})

def login_view(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None:

            login(request, user)

            return redirect('allcards')
        else:
            return HttpResponse("invalid login credentials")
    
    return render(request, 'django_registration/login.html')

@login_required      
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required 
def card(request,card_id):
    try:
        card = FlashCard.objects.get(id =card_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-pics/pic.html", {"card":card})
@login_required
def uploadcard(request,user_id):
    if request.method=="post":
        form=CommentForm(request.POST, instance=request.user)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            title = form.cleaned_data['title']
            text= form.cleaned_data['text']
            card=FlashCard(subject=subject,title=title,text=text,user=request.user)
            Flashcard.card.save_card()
            print(card)
            HttpResponseRedirect('allcards')
    else:
        form = CommentForm()
    return render(request, 'uploadcard.html', {"form":form})

@login_required
def allcards(request):
    cards=FlashCard.objects.all()
    return render(request, 'allcards.html', {"cards":cards})

@login_required
def search_results(request):

    if 'card' in request.GET and request.GET["card"]:
        search_term = request.GET.get("card")
        searched_cards =FlashCard.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all/search.html',{"message":message,"cards": searched_cards})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all/search.html',{"message":message})
