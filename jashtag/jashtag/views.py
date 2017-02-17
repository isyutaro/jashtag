# coding: utf-8
from annoying.decorators import render_to


@render_to('home.html')
def home(request):
    resultado = False
    if request.method == 'POST':
        jashtag = request.POST.get('jashtag', None)
        if jashtag:
            resultado = jashtag
        else:
            resultado = False

    return {'jashtag': resultado}

