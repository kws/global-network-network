from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'site_name': "Skillsfinder",
    }
    return render(request, 'skillsfinder/index.html', context)
