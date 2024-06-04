from django.shortcuts import render, redirect
from .models import Logo, Info,Background, About, Track, Reviws, ContactUs

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactUs.objects.create(name=name,email=email,message=message)
        return redirect('index')
    
    logo = Logo.objects.first()
    info = Info.objects.first()
    back = Background.objects.first()
    about = About.objects.first()
    track = Track.objects.first()
    review = Reviws.objects.first()

    return render(request, 'main/index.html', context= {
        'logo':logo,
        'info':info,
        'back':back,
        'about':about,
        'track':track,
        'review':review

    })