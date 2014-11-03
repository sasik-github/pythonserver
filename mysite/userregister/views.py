from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from userregister.models import User
from userregister.forms import UserForm

import datetime


class IndexView(generic.ListView):
    """docstring for IndexView"""
    template_name = 'userregister/list.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.all()
    


def register_form(request):
    errors = []
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User(
                name = cd['name'],
                borndate = cd['borndate'],
                age = cd['age'],
                job = cd['job'],
                created_at = cd['created_at']
                )
            print user
            user.save()
            return redirect('index')
    else:
        form = UserForm(
            initial = {'created_at': datetime.datetime.now}
            )
    return render(request, 'userregister/register_form.html', {'form': form})