from django.shortcuts import render
from rest_framework.response import Response

from .models import Demo
from .serializers import DemoSeriallizer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view




# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def demo_list(request):
    print("function is called!!")
    if request.method == "GET":
        demo = Demo.objects.all()
        serializer = DemoSeriallizer(demo , many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DemoSeriallizer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



@api_view(['GET','PUT','DELETE'])
def demo_detail(request,pk):
    demo = Demo.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = DemoSeriallizer(demo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DemoSeriallizer(demo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        demo.delete()
        return Response("deleted")

