from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'^$',views.welcome,name = "welcome"),
    url(r'login/',views.login_view,name="login"),
    path('register/', views.registerPage, name="django_registration_register"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^uploadcard/(\d+)',views.uploadcard,name ='uploadcard'),
    url(r'^card/(\d+)',views.card,name ='card'),
    url(r'^cards/',views.allcards,name ='allcards'),
    path('logout/', views.logout_view, name="logout"),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='change-password.html'),name='password_reset'), 


]