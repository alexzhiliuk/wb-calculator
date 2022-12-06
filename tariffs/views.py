from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Product


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = "categories"
    template_name = "tariffs/tariffs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        if request.GET.get("category"):
            context["categories"] = context["categories"].filter(title__contains=request.GET["category"])
        
        if request.GET.get("product"):
            context["product_search"] = request.GET["product"]

        return context


def calculator(request):

    return render(
        request,
        "tariffs/calculator.html"
    )