# coding: utf-8

from django.shortcuts import render

def index(request, **vargs):            
  return render(request, 'index.html', {})
