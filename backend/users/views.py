from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, UserSerializer, EmailTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()


class RegisterView(generics.CreateAPIView):
	serializer_class = RegisterSerializer
	permission_classes = [permissions.AllowAny]


class MeView(generics.RetrieveAPIView):
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user


class EmailTokenObtainPairView(TokenObtainPairView):
	serializer_class = EmailTokenObtainPairSerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def google_oauth_login(request):
	"""
	Placeholder for Google OAuth token exchange.
	Accepts { id_token } from client, verifies it, and returns JWT pair.
	For Phase 1, this returns 400 until Google OAuth is configured.
	"""
	return Response({"detail": "Google OAuth not configured yet. Provide id_token and we will implement verification."}, status=400)

