# coding: utf-8
from annoying.decorators import render_to


@render_to('home.html')
def home(request):
    q = ''
    if 'jashtag' in request.GET:
        q = request.GET['jashtag']
        print "valor: ", q
    return {'jashtag': q}
