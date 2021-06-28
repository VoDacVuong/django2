from django.db.models.aggregates import Count
from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from rest_framework import serializers
from . import serializersu
import user

@api_view(['GET'])
def index(req):
    listUser = [
         {'name': "Nguyen A", 'email': "A@gmail.com", 'phone': "7141414141"}, 
         {'name': "Nguyen B", 'email': "B@gmail.com", 'phone': "8141174747"},
         {'name': "Nguyen C", 'email': "C@gmail.com", 'phone': "7575757774"}, 
         {'name': "Nguyen D", 'email': "D@gmail.com", 'phone': "5575774555"}, 
         {'name': "Nguyen E", 'email': "E@gmail.com", 'phone': "6555454545"}, 
         {'name': "Nguyen F", 'email': "F@gmail.com", 'phone': "7787878787"}, 
         {'name': "Nguyen G", 'email': "G@gmail.com", 'phone': "3989898989"}, 
         {'name': "Nguyen H", 'email': "H@gmail.com", 'phone': "8212121212"}, 
         {'name': "Nguyen I", 'email': "I@gmail.com", 'phone': "3010101440"}, 
         {'name': "Nguyen K", 'email': "K@gmail.com", 'phone': "2686868686"}
    ]
    return Response(listUser)

@api_view(['GET'])
def listUser(req):
    user = models.User.objects.all()
    serializers = serializersu.UserSerializers(user, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def listProfile(req):
    pro = models.Profile.objects.all()
    serializers = serializersu.ProfileSerializers(pro, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def listOrder(req):
    order = models.Order.objects.all()
    serializers = serializersu.OrderSerializers(order, many = True)
    return Response(serializers.data)

@api_view(['GET'])
def listDetailUser(req, key):
    arr = []
    for x in models.User.objects.all():
        arr.append(x.id)
    if key in arr:
        user = models.User.objects.get(id = key)
        serializers = serializersu.UserSerializers(user)
        return Response(serializers.data)
    else:
        return Response("Not found ID!")

@api_view(['POST'])
def CreateUser(req):
    serializers = serializersu.UserSerializers(data=req.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response("Not is value!")

@api_view(['POST'])
def CreateProfile(req):
    serializers = serializersu.ProfileSerializers(data=req.data)
    if serializers.is_valid():
        serializers.save()
    return Response

@api_view(['POST'])
def CreateProfile(req):
    # print(req.data['user'])
    arr = []
    for x in models.User.objects.all():
        arr.append(x.id)
    if req.data['user'] in arr:
        serializers = serializersu.ProfileSerializers(data=req.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
    else:
        return Response("Not is user!")



