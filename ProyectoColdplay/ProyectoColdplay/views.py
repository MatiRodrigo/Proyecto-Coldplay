from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "pages/index.html"

class Nosotros(TemplateView):
    template_name = "pages/nosotros.html"

class Productos(TemplateView):
    template_name = "pages/productos.html"
    
class Formulario(TemplateView):
    template_name = "pages/formulario.html"

