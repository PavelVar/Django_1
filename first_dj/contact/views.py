from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.views.generic import DetailView, UpdateView, DeleteView


def contact_home(request):
    error = ''
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        else:
            error = 'Error message'

    form = MessageForm()
    data = {'form': form, 'error': error, 'title': 'Contact us'}
    return render(request, 'contact/contacts.html', data)
