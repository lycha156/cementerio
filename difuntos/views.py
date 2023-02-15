from django.shortcuts import render

def index(request):
    return render(request, 'difuntos/index.html')

def create(request):
    pass

def update(request, id=id):
    pass

def show(request, id=id):
    pass

def delete(request, id=id):
    pass