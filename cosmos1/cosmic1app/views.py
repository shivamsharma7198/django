from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import Cosmos
from django.http import JsonResponse
from django.urls import reverse_lazy
from rest_framework import serializers
# Create your views here.
from .forms import CosmicForm

class CosmicCreate(CreateView):
    model = Cosmos
    template_name = 'cosmic_create.html'
    # form = CosmicForm
    # queryset = Cosmos.objects.all()
    fields = '__all__'
def apiOverview(request):
    """

    """
    return JsonResponse("API BASE POINT",safe = False)

class CosmicList(ListView):
    # model = Cosmos
    template_name = 'cosmic_list.html'
    queryset = Cosmos.objects.all()

class CosmicDetail(DetailView):
    model = Cosmos
    template_name = 'cosmic_detail.html'
    # queryset = Cosmos.objects.all()
    # def get_object(self):
    #     id = self.kwargs.get("id")
    #     return get_object_or_404(Cosmos,id=id)

class CosmicDelete(DeleteView):
    model = Cosmos
    template_name = 'cosmic_delete.html'
    success_url = reverse_lazy('cosmic-list')

class CosmicUpdate(UpdateView):
    model = Cosmos
    template_name = 'cosmic_update.html'
    fields = '__all__'
    success_url = reverse_lazy('cosmic-list')