from django.conf.urls import url
from htdw import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^artist_statement/', views.artist_statement, name='artist_statement'),
    url(r'^performance/', views.performance, name='performance'),
    url(r'^film/', views.film, name='film'),
    url(r'^work/', views.work, name='work'),
    url(r'^social_practice/', views.social_practice, name='social_practice'),
    url(r'^harmless/', views.harmless, name='harmless'),
    url(r'^cv/', views.cv, name='cv'),
    url(r'^contact/', views.contact, name='contact'),
]
