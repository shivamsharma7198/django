from django.urls import path
from . import views
# from . import forms
urlpatterns = [
    path('', views.train_view, name='TrainList'),
    path('train/<int:pk>/',views.train_detail,name="Train_Detail")
    # path('train/new/',views.train_new,name="train_new")
]