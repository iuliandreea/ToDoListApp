from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('complete', views.complete, name="complete"),
    path('incomplete', views.incomplete, name="incomplete"),
    path('update/<str:id>/', views.update, name="update"),
    path('delete/<str:id>/', views.delete, name="delete")
]