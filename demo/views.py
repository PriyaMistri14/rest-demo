from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Demo
from .serializers import DemoSeriallizer,UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,action
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import  reverse
from rest_framework import renderers
from rest_framework import viewsets

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

# ........................functional based view.........................

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


@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def demo_detail(request,pk):
    print("//////////////////////////////", pk)
    try:
        demo = Demo.objects.get(pk=pk)
    except Demo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    print(demo)

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




#     ............................class based view..........................


class DemoList(APIView):
    def get(self, request):
        demo = Demo.objects.all()
        serializer = DemoSeriallizer(demo,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = DemoSeriallizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




class DemoDetail(APIView):
    def get(self, request, pk):
        demo = Demo.objects.get(pk=pk)
        serializer = DemoSeriallizer(demo)
        print("Created ........")
        return Response(serializer.data)


    def put(self,request, pk):
        demo =Demo.objects.get(pk=pk)
        serializer = DemoSeriallizer(demo, data= request.data)
        if serializer.is_valid():
            serializer.save()
            print("Updated ........")
            return Response(serializer.data)

        return Response(serializer.errors)


    def delete(self, request,pk):
        demo = Demo.objects.get(pk=pk)
        demo.delete()
        print("Deleted ........")
        return Response(status=status.HTTP_204_NO_CONTENT)




# ........................mixin and generic......................

class DemoListMixin(mixins.CreateModelMixin, mixins.ListModelMixin, generics.DestroyAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSeriallizer

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*argus,**kwargs):
        return self.create(request,*argus,**kwargs)




class DemoDetailMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSeriallizer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



#     .......................generics class based view........................

class DemoListGeneric(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Demo.objects.all()
    serializer_class = DemoSeriallizer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DemoDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]
    queryset = Demo.objects.all()
    serializer_class = DemoSeriallizer




# .............................user class....................
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





@api_view(['GET'])
def api_root(request):
    return Response({
        'demo' : reverse("demo_list",request=request),
        'user' : reverse("user_list",request=request)
    })





# ....................................renderer..................................
class DemoHighlight(generics.GenericAPIView):
    queryset= Demo.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self,request,*args,**kwargs):
        demo = Demo.objects.all()
        return Response(demo)




# .....................................viewsets..............................
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DemoViewSet(viewsets.ModelViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSeriallizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        demo = Demo.objects.all()
        return Response(demo)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)














