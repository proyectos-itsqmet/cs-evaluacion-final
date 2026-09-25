from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import Telefono
from .forms import TelefonoForm
from .services.telefono_service import load_telefonos

def telefono_list(request):
    load_telefonos()
    telefonos = Telefono.objects.all().order_by("id")
    paginator = Paginator(telefonos, 12)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "telefonos/telefono_list.html", {"page_obj": page_obj})

def telefono_detail(request, id):
    telefono = get_object_or_404(Telefono, id = id)
    return render(request, "telefonos/telefono_detail.html", {"telefono": telefono})

def telefono_create(request):
    if request.method == "POST":
        form = TelefonoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "telefonos/telefono_detail.html", {"telefono": form.instance})
    else:
        form = TelefonoForm()
    return render(request, "telefonos/telefono_form.html", {"form": form})

def telefono_update(request, id):
    telefono = get_object_or_404(Telefono, id = id)
    if request.method == "POST":
        form = TelefonoForm(request.POST, instance = telefono)
        if form.is_valid():
            form.save()
            return render(request, "telefonos/telefono_detail.html", {"telefono": form.instance})
    else:
        form = TelefonoForm(instance = telefono)
    return render(request, "telefonos/telefono_form.html", {"form": form})

def telefono_delete(request, id):
    telefono = get_object_or_404(Telefono, id = id)
    telefono.delete()
    return redirect("telefono_list")
