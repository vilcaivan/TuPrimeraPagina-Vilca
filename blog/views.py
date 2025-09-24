from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm

def home(request):
    return render(request, 'base.html')

def add_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Agregar Autor'})

def add_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Agregar Categoría'})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Agregar Post'})
