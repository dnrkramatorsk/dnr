# coding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from models import CallForm

@login_required
def index(request, **vargs):
    message = ""
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            message = u"Зарегистрировано! %s" % form.title
            form = CallForm()
    else:
        form = CallForm()

    return render(request, 'callcenter.html', {'form':form, "message":message})
