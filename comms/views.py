from django.shortcuts import render, redirect

# Create your views here.
def mainPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "comms/board.html", context)