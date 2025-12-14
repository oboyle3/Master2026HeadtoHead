from django.contrib import admin
from django.urls import path, include
from Master2026HeadtoHead import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('updateslot1/', views.updateslot1, name='updateslot1'),
    path('updateslot2/', views.updateslot2, name='updateslot2'),
    path('updateslot3/', views.updateslot3, name='updateslot3'),
    path('updateslot4/', views.updateslot4, name='updateslot4'),
    path('updateslot5/', views.updateslot5, name='updateslot5'),
]
