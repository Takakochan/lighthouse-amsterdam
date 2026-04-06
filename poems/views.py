from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Poem
from .forms import PoemForm
from events.models import Event


def home(request):
    recent_poems = Poem.objects.filter(is_published=True)[:3]
    upcoming_events = Event.objects.all()[:3]
    return render(request, 'home.html', {
        'recent_poems': recent_poems,
        'upcoming_events': upcoming_events,
    })


def poem_list(request):
    poems = Poem.objects.filter(is_published=True)
    return render(request, 'poems/poem_list.html', {'poems': poems})


def poem_detail(request, pk):
    poem = get_object_or_404(Poem, pk=pk, is_published=True)
    return render(request, 'poems/poem_detail.html', {'poem': poem})


@login_required
def poem_create(request):
    if request.method == 'POST':
        form = PoemForm(request.POST)
        if form.is_valid():
            poem = form.save(commit=False)
            poem.author = request.user
            poem.save()
            messages.success(request, 'Your poem has been posted.')
            return redirect('poem_detail', pk=poem.pk)
    else:
        form = PoemForm()
    return render(request, 'poems/poem_form.html', {'form': form, 'action': 'Post'})


@login_required
def poem_edit(request, pk):
    poem = get_object_or_404(Poem, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PoemForm(request.POST, instance=poem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your poem has been updated.')
            return redirect('poem_detail', pk=poem.pk)
    else:
        form = PoemForm(instance=poem)
    return render(request, 'poems/poem_form.html', {'form': form, 'action': 'Edit'})


@login_required
def poem_delete(request, pk):
    poem = get_object_or_404(Poem, pk=pk, author=request.user)
    if request.method == 'POST':
        poem.delete()
        messages.success(request, 'Your poem has been deleted.')
        return redirect('poem_list')
    return render(request, 'poems/poem_confirm_delete.html', {'poem': poem})
