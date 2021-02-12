from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Movie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def list_view(request):
    if request.method == "GET":
        print("GET")
        data = Movie.objects.all()
        print(Movie.objects.all())
        serializer = MovieSerializer(data,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@csrf_exempt
def detail_view(request, pk):
    try:
        snippet = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HTTPResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(snippet)
        # print("detail_get")
        return Response(serializer.data)
@api_view(['POST'])
def update_view(request,pk):
    movie_data = Movie.objects.get(pk =pk)
    serializer = MovieSerializer(instance=movie_data,data=request.data)
    if serializer.is_valid():
        serializer.save()
        # return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.data)

@api_view(['DELETE'])
def delete_view(request,pk):
    movie_data = Movie.objects.get(pk =pk)
    movie_data.delete()
    return Response("Item successfully deleted")