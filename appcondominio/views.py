from django.shortcuts import render
from django.contrib import messages
from .forms import *
from appcondominio.models import *
# Create your views here.
from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def residente_list(request):
    residentes = Residente.objects.all()
    return render(request, 'blog/residente_list.html', {'residentes': residentes})


def residente_detail(request, pk):
    residente = get_object_or_404(Residente, pk=pk)
    return render(request, 'blog/residente_detail.html', {'residente': residente})


@login_required
def residente_new(request):
    if request.method == "POST":
        form = ResidenteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            #post.published_date = timezone.now()
            post.save()
            return redirect('residente_detail', pk=post.pk)
    else:
        form = ResidenteForm()
    return render(request, 'blog/residente_edit.html', {'form': form})


@login_required
def residente_edit(request, pk):
    residente = get_object_or_404(Residente, pk=pk)
    if request.method == "POST":
        form = ResidenteForm(request.POST, instance=residente)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('residente_detail', pk=post.pk)
    else:
        form = ResidenteForm(instance=residente)
    return render(request, 'blog/residente_edit.html', {'form': form})

@login_required
def residente_remove(request, pk):
    residente = get_object_or_404(Ressidente, pk=pk)
    residente.delete()
    return redirect('residente_list')


def mes_list(request):
    meses = Mes.objects.all()
    return render(request, 'blog/mes_list.html', {'meses': meses})








def mes_detail(request, pk):
    mes = get_object_or_404(Mes, pk=pk)
    return render(request, 'blog/mes_detail.html', {'mes': mes})







@login_required
def mes_new(request):
    if request.method == "POST":
        form = MesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            #post.published_date = timezone.now()
            post.save()
            return redirect('mes_detail', pk=post.pk)
    else:
        form = MesForm()
    return render(request, 'blog/mes_edit.html', {'form': form})








@login_required
def mes_edit(request, pk):
    mes = get_object_or_404(Mes, pk=pk)
    if request.method == "POST":
        form = MesForm(request.POST, instance=mes)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('mes_detail', pk=mes.pk)
    else:
        form = MesForm(instance=mes)
    return render(request, 'blog/mes_edit.html', {'form': form})





@login_required
def mes_remove(request, pk):
    mes = get_object_or_404(Mes, pk=pk)
    mes.delete()
    return redirect('mes_list')


def pago_list(request):
    pagos = Pago.objects.all()
    return render(request, 'blog/pago_list.html', {'pagos': pagos})



def pago_new(request):
    if request.method == "POST":
        formulario = PagoForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            user = User.objects.get(username=request.user.username)
            post.empleado=user
            post.save()

            #postr = formulario.save(commit=False)
            #residenter = Residente.objects.get(nombre=request.residente.nombre)
            #postr.residente=residenter
            #postr.save()


            #pago = Pago.objects.create(empleado=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for residente_id in request.POST.getlist('residente'):
                for mes_id in request.POST.getlist('meses'):
                    factura = Factura(mes_id=mes_id, pago_id = user.id,residente_id=residente_id)
                    factura.save()
                    return redirect('factura_list')


            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = PagoForm()
    return render(request, 'blog/pago_new.html', {'formulario': formulario})


def factura_list(request):
    facturas = Factura.objects.all()
    return render(request, 'blog/factura_list.html', {'facturas': facturas})
