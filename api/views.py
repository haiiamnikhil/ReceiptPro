from codecs import encode
import re
from django.shortcuts import render
from .serializers import *
from rest_framework.parsers import JSONParser, FileUploadParser, FormParser
from app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


@csrf_exempt
def userRegisterForm(request):
    if request.method == 'POST':
        user = UserModel.objects.create(username=request.POST.get('username'),
                                        password=make_password(
                                            request.POST.get('password')),
                                        email=request.POST.get('email'),
                                        first_name=request.POST.get(
                                            'first_name'),
                                        last_name=request.POST.get(
                                            'last_name'),
                                        gender=request.POST.get('gender'),
                                        profile_image=request.FILES.get('profile_image'))
        return JsonResponse({"status": True, "data": "serializer.data"}, status=200, safe=False)


def userRegestrationsView(request):
    return render(request, "register.html")


@csrf_exempt
def userLoginForm(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            username=data['username'], password=data['password'])
        print(user)
        if user:
            login(request, user)
            print('loginSuccess')
            return JsonResponse({"message": "Login SuccessFull", "login_status": True, "user": request.user.username}, safe=False, status=200)
        else:
            return JsonResponse({"message": "Entered Credentials is Incorrect", "login_status": False}, safe=False, status=200)

@csrf_exempt
def userLoginView(request):
    return render(request, 'login.html')


@csrf_exempt
def selfUserProfile(request):
    if request.method == 'GET':
        details = UserModel.objects.filter(username=request.user)
        serializer = UserProfile(details, many=True)
        return JsonResponse(list(serializer.data), safe=False, status=200)
    elif request.method == 'POST':
        is_user = request.user.is_authenticated
        return JsonResponse({'is_user': is_user}, safe=False, status=200)


def selfUserProfileView(request, username):
    return render(request, "profile.html")


@csrf_exempt
def checkUser(request):
    if request.method == 'GET':
        return JsonResponse(request.user.username, safe=False, status=200)


def userDashboard(request):
    return render(request, "dashboard.html")


def employeeProfileView(request, username):
    user = UserModel.objects.get(username=username)
    return render(request, "employeeprofile.html")


@csrf_exempt
def employeeProfile(request, username):
    if request.method == 'POST':
        user = UserModel.objects.filter(username=username)
        print(user)
        serializer = UserProfileView(user, many=True)
        return JsonResponse(list(serializer.data), safe=False, status=200)


@csrf_exempt
def ListUsersView(request):
    if request.method == 'GET' and request.user.is_authenticated:
        details = UserModel.objects.all()
        serializer = ListUsers(details, many=True)
        return JsonResponse(list(serializer.data), safe=False, status=200)
    else:
        pass


def listUsers(request):
    return render(request, "listuser.html")


@csrf_exempt
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({"success": True}, safe=False, status=200)
