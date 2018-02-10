# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# the index function is called when root is visited
#/ - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
def register(request):
    response = "'placeholder for users to create a new user record"
    return HttpResponse(response)

#/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

#/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.
def users(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

    # /register - display 'placeholder for users to create a new user record'
    # /login - display 'placeholder for users to login' 
    # /users/new - have the same method that handles /register also handle the url request of /users/new
    # /users - display 'placeholder to later display all the list of users'
    