from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

# from django.db.models.functions import TruncMonth

# from django.db.models import Count

from django.urls import reverse_lazy

from item.models import Item, Comment

from .models import *

from .forms import *

from core.models import Messages

from django.contrib.auth.forms import UserChangeForm

from django.core.paginator import Paginator

# Create your views here.




@login_required(login_url='signin')
def index(request):
    items = Item.objects.filter(created_by=request.user)
    comment = Comment.objects.filter(name=request.user)
    mess = Messages.objects.filter(user=request.user)
    events = Events.objects.all()
    info = Info.objects.filter(user=request.user, status=False).order_by('-id')

    return render(request, 'dashboard/index.html', {
        'items': items,
        'comment': comment,
        'mess': mess,
        'username': request.user.username,
        'events': events,
        'info': info,

    })

@login_required(login_url='signin')
def profile(request):
    profile_instance = Profile.objects.filter(user=request.user).first()
    user_instance = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        user_form = UserForm(request.POST, instance=user_instance)
   
        if form.is_valid() and user_form.is_valid():
            # Update profile model fields
            profile_instance = form.save(commit=False)
            profile_instance.user = user_instance
            profile_instance.save()

            # Update user model fields
            user_instance.email = user_form.cleaned_data['email']
            user_instance.first_name = user_form.cleaned_data['first_name']
            user_instance.last_name = user_form.cleaned_data['last_name']
            user_instance.save()

            return redirect('dashboard:profile')
    else:
        initial_data = {
            'username': user_instance.username,
            'email': user_instance.email,
            'first_name': user_instance.first_name,
            'last_name': user_instance.last_name,
            
        }
        form = ProfileForm(instance=profile_instance, initial=initial_data)
        user_form = UserForm(instance=user_instance)


    return render(request, 'dashboard/profile.html', {
        'form': form,
        'profile': profile_instance,
        'user_form': user_form,
        'title': 'Your Profile',
    })

@login_required(login_url='signin')
def delete(request, pk):
    delete = get_object_or_404(Profile.image, pk=pk, user=request.user)

    if request.method == 'POST':
        delete.delete()
        return redirect('dashboard:profile')

    return render(request, 'dashboard/profile.html', {
        'delete': delete,
        'title': 'Confirm Delete',
    })

# def render_profile_image(request):
#     profile = Profile.objects.filter(user=request.user).first()

#     return render(request, 'dashboard/base.html', {
#         'profile': profile,
#     })

@login_required(login_url='signin')
def dashboard(request):
    # items = Item.objects.filter(created_by=request.user).order_by('?')  # To randomize the listing order
    items = Item.objects.filter(created_by=request.user).order_by('-id')

    paginate = Paginator(Item.objects.filter(created_by=request.user).order_by('?'), 6)
    page= request.GET.get('page')
    itemss = paginate.get_page(page)

    return render(request, 'dashboard/dashboard.html', {
        'items': items,
        'itemss': itemss,
        'title': 'Your Uploads',
    })

@login_required(login_url='signin')
def products(request):
    items = Item.objects.all().order_by('-id')  

    paginate = Paginator(items, 9)  
    page = request.GET.get('page')
    itemss = paginate.get_page(page)

    return render(request, 'dashboard/products.html', {
        'items': items,
        'itemss': itemss,
        'title': 'all Uploads',

    })

# @login_required(login_url='signin')
# def info(request, pk):
#     info = Info.objects.filter(user=request.user).order_by('-id')

#     return render(request, 'dashboard/info.html', {
#         'info': info
#         })

@login_required(login_url='signin')
def info(request, pk):
    # Retrieve the specific message based on the pk and user
    message = get_object_or_404(Info, id=pk, user=request.user)

    # Update the status to mark the message as read
    message.status = True
    message.save()

    return render(request, 'dashboard/info.html', {
        'message': message,
        'title': 'Message',

    })

@login_required(login_url='signin')
def allinfo(request):
    allinfo = Info.objects.filter(user=request.user).order_by('id')

    return render(request, 'dashboard/allinfo.html', {
        'allinfo': allinfo,
        'title': 'All Messages',

        })