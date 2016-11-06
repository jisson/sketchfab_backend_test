from django.conf.urls import patterns, url
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from sketchfab.views import LoginView, LogoutView

urlpatterns = patterns('sketchfab.views',
                       url(r'^register/$', CreateView.as_view(
                           template_name='sketchfab/register.html',
                           form_class=UserCreationForm,
                           success_url='/'
                       ), name='register'),
                       url(r'^login/$', LoginView.as_view(), name='login'),
                       url(r'^logout/$', LogoutView.as_view(), name='logout'),

                       url(r'^badges/$', 'badges', name='badges'),
                       url(r'^model3d/(?P<slug>[\.\w-]+)/$', 'see_model3d', name='see_model3d')
                       )
