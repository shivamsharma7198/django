from django.shortcuts import render,get_object_or_404
from .models import Train
# from . import forms


def train_view(request):
    train = Train.objects.all()
    context = {
        'trains' : train
    }
    return render(request,'trainlist.html',context)

def train_detail(request,pk):
    train_details = get_object_or_404(Train,pk=pk)
    # return render(request,'traindetails.html',train_details)
    # train_details = Train.objects.get(pk)
    context = {
        'train': train_details
    }
    return render(request,'traindetails.html',context)
#
# def train_new(request):
#     form = PostForm()
#     return render(request,'Train_edit.html',{'form':form})