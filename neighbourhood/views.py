from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .emails import *
# Create your views here.

def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')
    return render(request,'index.html')


@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)
    return render(request,'profile/user_profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
        return render(request,'profile/profile_form.html',{"form":form})
    

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'profile/update_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def defaulterer(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    defaulters = defaulter.objects.all()

    return render(request,'defaulter/defaulters.html',{"defaulters":defaulters})

@login_required(login_url='/accounts/login/')
def view_defaulter(request,id):
    current_user = request.user

    try:
        comments = Comment.objects.filter(post_id=id)
    except:
        comments =[]

    default = defaulter.objects.get(id=id)
    if request.method =='POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = current_user
            comment.post = default
            comment.save()
    else:
        form = CommentForm()

    return render(request,'defaulter/view_defaulters.html',{"defaulter":defaulter,"form":form,"comments":comments})


@login_required(login_url='/accounts/login/')
def new_defaulter(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =DefaulterForm(request.POST,request.FILES)
        if form.is_valid():
            defaulter = form.save(commit = False)
            defaulter.username = current_user
            defaulter.neighbourhood = profile.neighbourhood
            defaulter.save()

        return HttpResponseRedirect('/defaulters')

    else:
        form = DefaulterForm()

    return render(request,'defaulter/defaulter_form.html',{"form":form})


@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    # businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)
    businesses = Business.objects.all()


    return render(request,'business/businesses.html',{"businesses":businesses})

@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message=f"{search_term}"

        print(searched_businesses)

        return render(request,'business/search.html',{"message":message,"businesses":searched_businesses,"profile":profile})

    else:
        message="You haven't searched for any term"
        return render(request,'business/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def search_defaulters(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if 'defaulter' in request.GET and request.GET["defaulter"]:
        search_term = request.GET.get("defaulter")
        searched_defaulters = defaulter.search_defaulter(search_term)
        message=f"{search_term}"

        print(searched_defaulters)

        return render(request,'defaulter/search.html',{"message":message,"defaulters":searched_defaulters,"profile":profile})

    else:
        message="You haven't searched for any term"
        return render(request,'defaulter/search.html',{"message":message})
