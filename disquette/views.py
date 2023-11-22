from django.http import HttpResponse
from django.template import loader

from .models import Disquette


def index(request):
    random_disquette = Disquette.objects.order_by('?').first()
    template = loader.get_template('disquette/index.html')
    context = {
        'disquette': random_disquette,
        'langue': random_disquette.langue.nom,
    }
    return HttpResponse(template.render(context, request))
