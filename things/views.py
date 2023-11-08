from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Thing
from .permissions import IsOwnerOrReadOnly
from .serializers import ThingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class ThingList(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


@api_view(['GET', 'POST'])
def charge_webhook(request):
    if request.method == 'GET':
        return Response("this is get method")
    elif request.method == 'POST':
        print("object well receved")
        print(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def merchant_status_webhook_test(request):
    if request.method == 'GET':
        return Response("this is get method")
    elif request.method == 'POST':
        print("object well receved")
        print(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)

