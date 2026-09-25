from django.urls import path
from .views import *

urlpatterns = [
    path("", telefono_list, name = "telefono_list"),
    path("telefono/<int:id>", telefono_detail, name = "telefono_detail"),
    path("telefono/create", telefono_create, name = "telefono_create"),
    path("telefono/update/<int:id>", telefono_update, name = "telefono_update"),
    path("telefono/delete/<int:id>", telefono_delete, name = "telefono_delete"),
]
