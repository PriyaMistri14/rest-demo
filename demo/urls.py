from django.urls import path

from . import views
urlpatterns = [
    path('demo/', views.demo_list),
    path('demo/<int:pk>', views.demo_list),

]



