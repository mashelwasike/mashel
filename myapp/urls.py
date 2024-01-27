from django.urls import path
from . import views
from . import authview
from django.contrib.auth import views as auth_views


urlpatterns = [
     path('',views.home, name='home'),
     path('about/',views.about,name='about'),
     path('services/',views.services, name='services'),
     path('leadership/',views.leadership, name='leadership'),
     path('mission/',views.mission, name='mission'),
     path('values/',views.values, name='values'),
     path('services/',views.services, name='services'),
     path('news/',views.news, name='news'),
     path('create/',views.create,name='create'),

     #Authentication
     path('login/',authview.loginview, name='login'),
     path('register/',authview.register, name='signup'),
     path('logout/',authview.logoutview, name='logout'),

     #Backend
     path('category/',views.category,name='category'),
     path('category/<str:slug>/',views.categoryview,name='categoryview'),
     path('category/<str:cate_slug>/<str:prod_slug>/', views.productview, name='productview'),

     #reseting password
     path('reset_password/',auth_views.PasswordResetView.as_view(template_name="authentication/passwordreset.html"),name="reset_password"), 
     path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="authentication/passwordreset_sent.html"),
         name="password_reset_done"),
     path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="authentication/passwordreset_form.html"),
         name="password_reset_confirm"),
     path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="authentication/passwordreset_done.html"),
         name="password_reset_complete")
]