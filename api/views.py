from django.shortcuts import render
from .serializers import *
from rest_framework.parsers import JSONParser
from app.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, get_user_model,login, logout
from django.contrib.auth.decorators import login_required


@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = UserRegister(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status":True,"data":serializer.data},status=200,safe=False)
        else:
            # print(serializer.errors)
            return JsonResponse({"Error":"Username or Email Alredy Registerd"},status=200,safe=False)
    return render(request,"register.html")


@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(username=data['username'],password=data['password'])
        if user:
            login(request,user)
            print('loginSuccess')
            return JsonResponse({"message":"Login SuccessFull","login_status":True,"user":request.user.username},safe=False,status=200)
        else:
            return JsonResponse({"message":"Entered Credentials is Incorrect","login_status":False},safe=False,status=200)
    return render(request,'login.html')


@csrf_exempt
def userDetails(request):
    if request.method == 'GET':
        details = UserModel.objects.filter(username=request.user)
        serializer = UserProfile(details, many=True)
        return JsonResponse(list(serializer.data),safe=False,status=200)
    elif request.method == 'POST':
        is_user = request.user.is_authenticated
        return JsonResponse({'is_user': is_user},safe=False,status=200)
    
@csrf_exempt
def specificUser(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = UserModel.objects.get(username=data['username'])

@csrf_exempt   
def checkUser(request):
    if request.method == 'GET':
        return JsonResponse(request.user.username,safe=False,status=200)


def userDashboard(request):
    return render(request,"dashboard.html")


def userProfile(request,username):
    return render(request,"profile.html")

def userRenderView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = UserProfileView(data, many=True)
        return JsonResponse(list(serializer.data),safe=False,status=200)
    else:
         return JsonResponse(list("user"),safe=False,status=200)

def employeeprofile(request,username):
    user = UserModel.objects.get(username=username)
    return render(request,"employeeprofile.html")

@csrf_exempt
def employeeprofiledetails(request,username):
    if request.method == 'POST':
        user = UserModel.objects.filter(username=username)
        print(user)
        serializer = UserProfileView(user, many=True)
        return JsonResponse(list(serializer.data),safe=False,status=200)

@csrf_exempt
def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({"success":True},safe=False,status=200)
    

@csrf_exempt
def listUsers(request):
    return render(request,"listuser.html")

    

@csrf_exempt
def ListUsersView(request):
    if request.method == 'GET' and request.user.is_authenticated:
        details = UserModel.objects.all()
        serializer = ListUsers(details, many=True)
        return JsonResponse(list(serializer.data),safe=False,status=200)
    else:
        pass
    
@csrf_exempt
def uploadUserProfileImage(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfileImageUpload(data,many=True)
        return JsonResponse(list(serializer.data),safe=False,status=200)
    else:
        pass