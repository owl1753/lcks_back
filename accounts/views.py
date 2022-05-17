from asyncio.windows_events import NULL
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        search_email = data['email']
        obj = NULL
        try:
            obj = Account.objects.get(email=search_email)
        except Account.DoesNotExist:
            return HttpResponse(status=400)

        if data['password'] == obj.password:
            serializer = AccountSerializer(obj)
            return JsonResponse(serializer.data, safe=False)
        else:
            return HttpResponse(status=400)

    return HttpResponse(status=400)
            



