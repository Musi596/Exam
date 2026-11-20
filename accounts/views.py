from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Please fill all fields'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already used'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }, status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"detail": "Please fill all fields"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = authenticate(
        request,
        username=username,
        password=password,
    )

    return Response(
        get_tokens_for_user(user),
        status=status.HTTP_200_OK,
    )

@api_view(['POST'])
def logout_view(request):
    refresh = request.data.get('refresh')

    if not refresh:
        return Response({'error': 'Refresh token required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        token = RefreshToken(refresh)
        token.blacklist()

    except TokenError:
        return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh["username"] = user.username

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
