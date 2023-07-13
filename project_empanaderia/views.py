from django.views.generic import TemplateView


class Landing(TemplateView):
    template_name = "vinculos/landing_page.html"

class NuestrosProductos(TemplateView):
    template_name = "vinculos/nuestrosProductos.html"
class Contacto(TemplateView):
    template_name = "vinculos/contacto.html"

class Nosotros(TemplateView):
    template_name = "vinculos/nosotros.html"
