from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

from item.models import Category, Item, User

from django.contrib import messages

from .models import *

from .forms import CustomUserCreationForm, LoginForm, TodoForm, ReviewForm, MessagesForm

from django.core.paginator import Paginator

from django.db.models import Q

from hitcount.views import HitCountDetailView

from django.urls import reverse

# Create your views here.

class ItemDetailView(HitCountDetailView):
    model = Item
    template_name = 'dat.html'
    count_hit = True

def index(request):
    items = Item.objects.all().order_by('?')
    service = ServiceInfo.objects.all()
    service_list = ServiceList.objects.all()

   
    qi = request.GET.get('qi', '')
    if qi:
        items = Item.objects.filter(name__icontains=qi) | Item.objects.filter(description__icontains=qi) | Item.objects.filter(created_by__username__icontains=qi)

    categories = Category.objects.all()
    num_users = User.objects.count()  

    paginate = Paginator(items, 3)
    page= request.GET.get('page')
    itemss = paginate.get_page(page)

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = UserVisit(user=ip)
    print(ip)
    result = UserVisit.objects.filter(user__icontains=ip)
    if len(result) >= 1:
        # print("User exists")
        pass
    else:
        u.save()
        # print("User is Unique")
    count = UserVisit.objects.all().count()
    print("Total User is", count)



    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'itemss': itemss,
        'search_query': qi,
        'num_users': num_users,  
        'service': service,
        'service_list': service_list,
        'count': count,

    })

class PreventAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # List of URLs to prevent authenticated users from accessing
            restricted_urls = [reverse('signup'), reverse('signin')]

            # Redirect authenticated users away from restricted URLs
            if request.path in restricted_urls:
                return redirect('index')  # Redirect to the home page or another appropriate URL

        return response

def contact(request):
    cons = ContactInfo.objects.all().order_by('id')


    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user  # Set the current user
            message.save()
            messages.success(request, 'Your message was sent successfully!')
            return redirect('/contact/')
        else:
            messages.error(request, 'Sending failed. Please correct the errors below.')

    else:
        form = MessagesForm()

    return render(request, 'core/contact.html', {
        'form': form,
        'cons': cons,
        'title': 'Contact Us'
    })

def pricing(request):
    return render(request, 'core/pricing.html')

def about(request):
    num_users = User.objects.count()  
    items = Item.objects.all().order_by('?')
    team = Team.objects.all().order_by('-id')
    about = AboutInfo.objects.all().order_by('id')



    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review_instance = form.save(commit=False)
            review_instance.save()
            return redirect('core:about')  
        else:
            pass
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('?')  # Fetch all reviews

    paginate = Paginator(reviews, 5)
    page= request.GET.get('page')
    rev = paginate.get_page(page)

    return render(request, 'core/about.html', {
        # 'reviews': reviews,
        'rev': rev, 
        'form': form,
        'num_users': num_users,  
        'items': items,
        'team': team,
        'about': about,
        

        })

def todo(request):
    # Handling POST request (form submission)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_instance = form.save(commit=False)
            if request.user.is_authenticated:
                todo_instance.user = request.user  # Set the user for the todo
                todo_instance.save()
                return redirect('core:todo')  # Redirect to the todo view after saving
            else:
                # Redirect to login if the user is not authenticated
                return redirect('signin')
        else:
            # Handle form errors (you might want to pass the form back to the template)
            pass
    else:
        form = TodoForm()

    # Fetching todos for the current user
    todos = Todo.objects.filter(user=request.user) if request.user.is_authenticated else []

    # Render the template with the form and the list of todos
    return render(request, 'core/TODO.html', {
        'form': form, 
        'todos': todos,
        'title': 'Todos',

        })


def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('core:todo')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'core/TODO.html', {
        'form': form,
        'title': 'Edit Todo',
    })


def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)

    if request.method == 'POST':
        todo.delete()
        return redirect('core:todo')

    return render(request, 'core/TODO.html', {
        'todo': todo,
        'title': 'Confirm Delete',
    })




def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('/signin/')
        else:
            # If form is not valid, add an error message
            messages.error(request, 'Registration failed. Please correct the errors below.')
            form.non_field_errors()
            # Redirect to a specific ID on the members page
            return redirect('/signup/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'core/sign-up.html', {'form': form})


def terms(request):
    terms = Terms.objects.all()

    return render(request, 'core/terms.html', {
        'terms': terms,
        'title': 'Terms and Conditions',
    })

def privacy(request):
    privacy = Privacy.objects.all()

    return render(request, 'core/privacy.html', {
        'privacy': privacy,
        'title': 'Privacy Policy',
    })

