from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    news = News.objects.all()
    context = {
        'user': 'my lord',
        'news': news,
    }

    return render(request, 'landing/index.html', context)