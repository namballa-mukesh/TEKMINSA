from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")


def about(request):
    return render(request, "about.html")


def contact_us(request):
    return render(request, "contact_us.html")


def community_guidelines(request, *args):
    return render(request, "community_guidelines.html")


def cookie_policy(request):
    return render(request, "cookie_policy.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def user_agreement(request):
    return render(request, "user_agreement.html")
