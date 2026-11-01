"""Rutas del proyecto web de EcoTech Solutions."""

from django.urls import path

from sustentabilidad.views import vista_panel_sustentabilidad

urlpatterns = [
    path("", vista_panel_sustentabilidad, name="panel_sustentabilidad"),
    path("panel/", vista_panel_sustentabilidad),
]
