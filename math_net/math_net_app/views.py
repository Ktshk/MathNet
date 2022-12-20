from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'math_net_app/index.html')

def about(request):
    return render(request, 'math_net_app/about.html')
