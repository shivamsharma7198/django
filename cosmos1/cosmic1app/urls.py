from django.urls import path
from .views import CosmicList,CosmicDetail,CosmicCreate,CosmicDelete,CosmicUpdate

# app_name = 'cosmic1app'

urlpatterns = [
    path('',CosmicList.as_view(),name='cosmic-list'),
    path('create/',CosmicCreate.as_view(),name='cosmic-create'),
    path('<int:pk>/detail',CosmicDetail.as_view(),name='cosmic-detail'),
    path('<int:pk>/delete/',CosmicDelete.as_view(),name='cosmic-delete'),
    path('<int:pk>/update/',CosmicUpdate.as_view(),name='cosmic-update'),

]