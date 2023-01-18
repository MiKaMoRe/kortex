from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from users.models import User

class Profile(View):
    def get(self, request, slug):
        profile_queryset = User.objects.filter(slug=slug)[:1]
        if profile_queryset:
            ctx = dict(profile=profile_queryset[0])
            return render(request, "profiles/user.html", ctx)
        raise Http404
