# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import csrf

# Create your views here.
from django.urls import reverse

from django.views.generic import TemplateView
from django.contrib.auth.models import User


from system.forms import FeedBackForm
from django.contrib import auth


class HomeView(TemplateView):
    template_name = "index.html"

class Register(TemplateView):
    template_name = "register.html"

class ProfilePage(TemplateView):
    template_name = 'registration/profile.html'

class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        context={}
        if request.method == 'POST':
            message=None
            username=request.POST.get("username")
            fullname=request.POST.get("fullname")
            email=request.POST.get("email")
            password=request.POST.get("password")
            password2=request.POST.get("password2")

            if len(password)>8 and password==password2:
                user=User.objects.create_user(username,email,password)
                user.first_name=fullname
                user.save()
                message="User registered succesfully!"
                return redirect(reverse("login"))
            else:
                message="Error"
            context['message']=message
        return render(request, self.template_name,context)


from django.utils import timezone

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("/")


class FeedbackView(TemplateView):
    template_name = "feedback.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        form = FeedBackForm()
        if request.method=="POST":
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, u"Спасибо")
                return redirect(reverse("feedback"))

        context['feedback_form']=form
        return render (request, self.template_name, context)

class FeedView(TemplateView):
    template_name = 'feedbacks.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect("/")
        context ={
            'feedbacks':Feedback.objects.all()
        }
        return  render(request, self.template_name, context)

