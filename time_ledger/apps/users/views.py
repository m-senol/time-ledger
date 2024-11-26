from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from .serializers import UserSerializer
from django.views import View
from django.http import JsonResponse

# Create your views here.

class EmployeeLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and not user.is_manager:
            login(request, user)
            return redirect('employee_home_page')
        else:
            return render(request, 'employee_login.html', {'error': 'Invalid username or password'})

class ManagerLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_manager:
            login(request, user)
            return redirect('manager_home_page')
        else:
            return render(request, 'manager_login.html', {'error': 'Invalid username or password'})

class LogoutView(View):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('home')

class UserLeaveDaysView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"available_leave_days": request.user.available_leave_days})

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
