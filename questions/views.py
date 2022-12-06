from django.shortcuts import render, redirect
from django.urls import reverse
from questions.forms import *
from django.core.mail import send_mail
from django.conf import settings


def send_question(request):
    
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.user = request.user
            new_question.save()
        
        return redirect(reverse("edit"))

    return redirect(reverse("edit"))


def send_question_response(request, uid):

    if not request.user.is_superuser:
        return redirect(reverse("edit"))

    question = Question.objects.all().filter(id=uid).first()
    if not question:
        return redirect(reverse("edit"))

    if request.method == "POST":
        response = request.POST["response"]
        send_mail("Задачи", response, settings.EMAIL_HOST_USER, [question.user.email])
        question.status = 1
        question.save()
        return redirect(reverse("edit"))

    return render(
        request,
        "questions/send_response.html",
        {
            "question": question,
        }
    )
