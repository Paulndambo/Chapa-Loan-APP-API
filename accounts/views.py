from django.http import JsonResponse
from accounts.models import Customer, Income
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import CustomerSerializer, IncomeSerializer, RegisterSerializer, UserNamesUpdateSerializer, UserSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['id'] = user.id
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(routes)



class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data
        })
        

class UsersList(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get(self, request):
        user = self.request.user
        if user.is_superuser:
            users = User.objects.all()
            serializer = self.serializer_class(instance=users, many=True)
            print("User is Super User")
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        else:
            print("user is a normal user")
        return Response({"message": "User Fetched"})


class UserDetailAPIView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.username:
            instance.username = instance.username

    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class CustomerAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request):
        #customers = Customer.objects.all()
        user = self.request.user if self.request.user else request.user
        if user.is_superuser:
            customers = Customer.objects.all()
            serializer = self.serializer_class(instance=customers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            customers = get_object_or_404(Customer, user=user)
            serializer = self.serializer_class(instance=customers)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = self.request.user if self.request.user else request.user
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailAPIView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    lookup_field = "pk"


    def perfrom_destroy(self, instance):
        return super().perform_destroy(instance)
            

class IncomeAPIView(generics.GenericAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get(self, request):
        incomes = Income.objects.all()
        serializer = self.serializer_class(instance=incomes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request):
        user = self.request.user if self.request.user else request.user
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)