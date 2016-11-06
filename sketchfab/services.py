from django.shortcuts import get_object_or_404
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

import logging

__author__ = 'Pierre Rodier | pierre@buffactory.com'

logger = logging.getLogger('sketchfab')


def get_model_with_hit_count(request, klass, *args, **kwargs):
    """
    Retrieve a model object from the database and update the HitCount related to that object.

    :param request:     The request performed.
    :param klass:       May be a Model, Manager, or QuerySet object.

    All other passed arguments and keyword arguments are used in the get() query.

    :raise Http404: That method is based on django.shortcuts.get_object_or_404 method. So a Http404 exception could
    be raises if the object does not exist.

    :return:    An object matching the query.
    """

    model = get_object_or_404(klass, *args, **kwargs)
    hit_count = HitCount.objects.get_for_object(model)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    logger.debug(hit_count_response)
    return model
