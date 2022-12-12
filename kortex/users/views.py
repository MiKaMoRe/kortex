from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from users.models import User
from users.forms import *


class SignUp(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "users/sign_up.html"

    def success_url(self, slug):
        return reverse_lazy("profile", kwargs={"slug": slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sign_up"] = True
        return context

    def form_valid(self, form):
        form.save()
        email = self.request.POST["email"]
        password = self.request.POST["password1"]
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return redirect(self.success_url(user.slug))


class SignIn(LoginView):
    model = User
    authentication_form = UserSignInForm
    template_name = "users/sign_in.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sign_in"] = True
        return context

    def get_success_url(self) -> str:
        next_url = self.request.POST.get("next")
        if next_url:
            return next_url
        slug = self.request.user.slug
        return reverse_lazy("profile", kwargs={"slug": slug})
