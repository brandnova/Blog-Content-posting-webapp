from django.contrib.auth.decorators import login_required

from django.db.models import Count

from django.shortcuts import redirect, render, get_object_or_404

from .forms import EditItemForm, NewItemForm, CommentForm

from .models import Category, Item, Comment

from dashboard.models import Profile

# Create your views here.

def items(request):
    category_id = request.GET.get('category', None)
    categories = Category.objects.annotate(item_count=Count('items'))  
    

    if category_id:
        filtered_items = Item.objects.filter(category_id=category_id)
    else:
        filtered_items = Item.objects.all()

    return render(request, 'item/items.html', {
        'categories': categories,
        'items': filtered_items,
        'category_id': int(category_id) if category_id else None,
        'title': 'All Uploads',

    })

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    comments = Comment.objects.filter(post=item)
    return render(request, 'details.html', {'post': item, 'comments': comments})

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)
    badge = Profile.badge

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.name = request.user  # Set the user from the request
                comment.item = item
                comment.save()
                return redirect('items:detail', pk=item.id)
            else:
                pass
    else:
        form = CommentForm()

    return render(request, 'item/detail.html', {
        'badge': badge,
        'item': item,
        'related_items': related_items,
        'form': form,
    })

@login_required(login_url='signin')  
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Post',
        })

@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Post',
        })

@login_required(login_url='signin')
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

def add_comment(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.name = request.user  # Set the user from the request
                comment.item = item
                comment.save()
                return redirect('items:detail', pk=item.id)
            else:
                pass
    else:
        form = CommentForm()

    return render(request, 'item/detail.html', {'form': form, 'item': item})

