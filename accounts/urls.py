from django.urls import path
from . import views
from . views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path('', views.getRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path("users/", UsersList.as_view(), name="users"),
    path("user/<int:pk>/details/", views.UserDetailAPIView.as_view(), name="user-details"),
    path("customers/", views.CustomerAPIView.as_view(), name="customers"),
    path("customers/<int:pk>/", views.CustomerDetailAPIView.as_view(), name="customers-details"),
    path("income/", views.IncomeAPIView.as_view(), name="income"),
]
