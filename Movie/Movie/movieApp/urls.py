from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_view,name = "list"),
    path('<int:pk>/', views.detail_view,name = "detail"),
    # path('create-view/',views.create_view,name = "create"),
    path('update/<int:pk>/',views.update_view,name = "update"),
    path('delete/<int:pk>/',views.delete_view,name = "delete"),

]