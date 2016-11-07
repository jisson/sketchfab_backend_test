from django.conf.urls import patterns, url
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from sketchfab.views import LoginView, LogoutView, Model3dFormView

urlpatterns = patterns('sketchfab.views',
                       url(r'^register/$', CreateView.as_view(
                           template_name='sketchfab/register.html',
                           form_class=UserCreationForm,
                           success_url='/'
                       ), name='register'),
                       url(r'^login/$', LoginView.as_view(), name='login'),
                       url(r'^logout/$', LogoutView.as_view(), name='logout'),

                       url(r'^badges/$', 'badges', name='badges'),

                       url(r'^model3d/create/$', login_required(Model3dFormView.as_view()), name='model3d_form'),
                       url(r'^model3d/(?P<slug>[\.\w-]+)/$', 'see_model3d', name='see_model3d'),
                       )
