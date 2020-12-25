from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import AadharSerializer
from .models import Aadhar
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
import json
from django.core.exceptions import ObjectDoesNotExist


class HomePageView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class UserCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                if request.data['user_type'] == 'manager':
                    print("SUPER",user)
                    user.is_staff = True
                    user.save()
                elif request.data['user_type'] == 'staff':
                    user.is_staff = False
                    user.save()
                json = serializer.data
                json['token'] = token.key
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_aadhar(request):
    user = request.user.id
    aadhar = Aadhar.objects.all()
    serializer = AadharSerializer(aadhar, many=True)
    return JsonResponse({'aadhar': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_aadhar(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        #aadhar = Aadhar.objects.get(id=payload["author"])
        aadhar = Aadhar.objects.create(
            AadharNumber=payload["AadharNumber"],
            is_Active=payload["is_Active"],
        )
        serializer = AadharSerializer(aadhar)

        return JsonResponse({'aadhar': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_aadhar(request, aadhar_number):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        aadhar_ = Aadhar.objects.filter(AadharNumber=aadhar_number)
        # returns 1 or 0
        aadhar_.update(**payload)
        aadhar = Aadhar.objects.get(AadharNumber=aadhar_number)
        serializer = AadharSerializer(aadhar)
        return JsonResponse({'aadhar': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_aadhar(request, aadhar_number):
    user = request.user.id
    try:
        aadhar = Aadhar.objects.get(AadharNumber=aadhar_number)
        aadhar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
