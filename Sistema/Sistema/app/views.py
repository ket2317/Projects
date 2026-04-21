from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Task
from .forms import CreateNewTask

def home(request):
    task = Task.objects.all()
    return render(request, 'index.html', {'task': task})

def Create_task(request):
    if request.method == 'POST':
        form = CreateNewTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = CreateNewTask()
    return render(request, 'create_task.html', {'form': form})

def delete_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id)
        task.delete()
    return redirect('/home/')

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = CreateNewTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = CreateNewTask(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def ver(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'ver.html', {'task': task})

def descargar_nota_pdf(request, id):
    task = get_object_or_404(Task, id=id)

    html_string = render_to_string('ver.html', {
        'task': task
    })

    pdf = HTML(
        string=html_string,
        base_url=request.build_absolute_uri('/')
    ).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="nota_pedido_{task.id:04d}.pdf"'
    return response

def SinPrevio(request):
    grabado = Task.objects.filter(estado='Sin previo')
    return render(request, 'SinPrevio.html', {'task': grabado})

def EnGrabado(request):
    grabado = Task.objects.filter(estado='Grabando')
    return render(request, 'grabando.html', {'task': grabado})

def Entregar(request):
    grabado = Task.objects.filter(estado='Entregar')
    return render(request, 'Entregar.html', {'task': grabado})