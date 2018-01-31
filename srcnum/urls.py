from django.conf.urls import url

from . import views

app_name = 'srcnum'

urlpatterns = [
    url(r'^$', views.index, name='index'),                                              #главная страница
    url(r'^contacts/$', views.contacts, name='contacts'),                               #страница контакты
    url(r'^get_number/$', views.get_number, name='get_number'),                         #URL формы
    url(r'^about/$', views.about, name='about')
]