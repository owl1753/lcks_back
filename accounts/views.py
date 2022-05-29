from asyncio.windows_events import NULL
from django.http import HttpResponse, JsonResponse
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
        obj = NULL
        error = {'email':'', 'password':''}

        if data['email'] == '' or data['password'] == '':
            return JsonResponse(error, status=400)

        try:
            obj = Account.objects.get(email=data['email'])
        except Account.DoesNotExist:
            error['email'] = '해당 이메일로 가입한 계정이 없습니다.'
            return JsonResponse(error, status=400)

        if data['password'] == obj.password:
            serializer = AccountSerializer(obj)
            return JsonResponse(serializer.data, safe=False)
        else:
            error['password'] = '비밀번호가 틀렸습니다.'
            return JsonResponse(error, status=400)

    return JsonResponse(error, status=400)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        obj = NULL
        error = {'email':'', 'name':'', 'password':'', 're_password':''}
        is_error = False

        if data['password'] == '':
            error['password'] = '필수 입력 항목입니다.'
            is_error = True

        if data['re_password'] == '':
            error['re_password'] = '필수 입력 항목입니다.'
            is_error = True

        if data['name'] == '':
            error['name'] = '필수 입력 항목입니다.'
            is_error = True

        if data['password'] != data['re_password'] and data['password'] != '' and data['re_password'] != '':
            error['re_password'] = '위의 비밀번호와 같지 않습니다.'
            is_error = True

        if data['email'] == '':
            error['email'] = '필수 입력 항목입니다.'
            is_error = True
        else:
            try:
                obj = Account.objects.get(email=data['email'])
                error['email'] = '이미 가입된 이메일 입니다.'
                is_error = True
            except Account.DoesNotExist:
                if is_error == False:
                    Account.objects.create(
                        email = data['email'],
                        name = data['name'],
                        password = data['password']
                    )
                    obj = Account.objects.get(email=data['email'])
                    serializer = AccountSerializer(obj)
                    return JsonResponse(serializer.data, safe=False)

        return JsonResponse(error, status=400)

    return HttpResponse(status=400)