from multiprocessing import context
from django.shortcuts import render


# Create your views here.
def main(request):
    context = {}

    return render(request, 'chat/main.html', context=context)