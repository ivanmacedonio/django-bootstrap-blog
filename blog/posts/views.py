from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    posts= Post.objects.all()#guardamos todos los posts en una variable
    context = {'posts' : posts} #cargamos la data en un context

    return render(request, 'index.html', context) #le enviamos dicho context para que pueda mostrarlo 

def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post':post}
    return render (request, 'postdetail.html', context)

def formcreate(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) #form almacena un modelo POSTFORM el cual almacena la info que llega por post desde el formulario al que hace render
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'form.html', context)

def delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST': #cuando damos a confirmar en deletetemplate el boton envia informacion por post,
        #entonces si llega post significa que lo elimino
        post.delete()
    context = {'post': post}
    return render(request, 'deletetemplate.html', context)

def update(request, pk):
    post = Post.objects.get(id=pk) #guarda el registro del post que coincida con el post en el que estamos situados
    form = PostForm(instance=post) #cargamos el formulario con la data que le llego a la variable post
    #al tocar update y ya estar cargada, el formulario se rellena solo y podemos hacer el post nuevamente mas facil 
    if request.method == 'POST': #si tocamos update 
        form = PostForm(request.POST, request.FILES, instance=post)#se guardan en form los datos (post) y archivos(files) que llegaron nuevos
        form.save()#los guarda
        return redirect('index')
    context= {"form": form}

    return render(request, 'form.html', context)
