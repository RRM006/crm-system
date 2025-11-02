from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    role = serializers.ChoiceField(choices=User.Roles.choices)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "role", "company", "brand"]
        read_only_fields = ["id"]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        username = validated_data.get("username")
        if not username:
            # default to email local-part if username not supplied
            email = validated_data.get("email", "")
            username = email.split("@")[0] if email else None
            validated_data["username"] = username
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "role", "company", "brand"]


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Accepts either username or email for login
    def validate(self, attrs):
        # map email -> username if provided
        email = self.initial_data.get("email")
        if email and not self.initial_data.get("username"):
            self.initial_data["username"] = email
        return super().validate(self.initial_data)
