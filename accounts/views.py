from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.forms import *
from questions.forms import QuestionForm
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                new_user = form.save(commit=False)
                new_user.username = new_user.email
                new_user.set_password(form.cleaned_data["password"])
                new_user.save()
            except:
                messages.info(request, "Пользователь с таким e-mail уже существует")
                return redirect(reverse("register"))

            new_user = authenticate(
                request,
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            login(request, new_user)

            return redirect(reverse("edit"))
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"user_form": form})


class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["email"], password=cd["password"]
            )
            if user is None:
                messages.info(request, "E-mail или пароль введены неверно")
                return redirect(reverse("login"))

            if not user.is_active:
                messages.info(request, "Вы заблокированы")
                return redirect(reverse("login"))

            login(request, user)
            return redirect(reverse("edit"))

        return render(request, "accounts/login.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})


@login_required
def edit(request):

    question_form = QuestionForm()
    if request.method == "POST":
        form = UserEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()

        return redirect(reverse("edit"))

    else:
        form = UserEditForm(instance=request.user)
    
    return render(
        request,
        "accounts/account.html",
        {
            "form": form,
            "q_form": question_form,
        }
    )


@login_required
def delete_user(request, uid):
    
    if request.user.id != uid:
        return redirect(reverse("edit"))

    request.user.delete()
    return redirect(reverse("register"))
