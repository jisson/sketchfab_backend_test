from django.conf.urls import patterns, url
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from sketchfab.views import LoginView, LogoutView

urlpatterns = patterns('sketchfab.views',
                       url('^register/$', CreateView.as_view(
                           template_name='sketchfab/register.html',
                           form_class=UserCreationForm,
                           success_url='/'
                       ), name='register'),
                       url('^login/', LoginView.as_view(), name='login'),
                       url(r'logout/$', LogoutView.as_view(), name='logout')
                       )
