from django.shortcuts import render
import connect
ms = connect.MongoService()
# Create your views here.
def home(request):
    return render(request, 'math_net_app/index.html', {'accs': ms.get_users()})

def about(request):
    return render(request, 'math_net_app/about.html', {'num': range(10000)})
