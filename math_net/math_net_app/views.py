from django.shortcuts import render
import connect
from .forms import LoginForm

ms = connect.MongoService()


# Create your views here.
def home(request):
    return render(request, 'math_net_app/index.html', {'accs': ms.get_users()})


def about(request):
    try:
        request.session.pop("username")
    except KeyError:
        print("Arleady no session!!!")
    return render(request, 'math_net_app/about.html', {'num': range(10000)})


def login(request):
    print("String 13,", request)
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_data = ms.check_user(form.cleaned_data.get("login"), form.cleaned_data.get("password"))
        if user_data != 0:
            request.session['username'] = form.cleaned_data.get("login")
            request.session['userid'] = str(user_data['_id'])
        else:
            return render(request, 'math_net_app/login.html', {"form": form, "msg": "Error of password or login"})
    sssr = request.session.get("username", None)
    if sssr is None:
        # Redirecting to login page
        return render(request, 'math_net_app/login.html', {"form": form})
    else:
        # Redirecting to home page
        return home(request)
