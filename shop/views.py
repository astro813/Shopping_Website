from django.views import generic
from .models import Cloth, Color

class IndexView(generic.ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        return Cloth.objects.all()


class DetailView(generic.DetailView):
    model = Cloth
    template_name = 'shop/detail.html'

