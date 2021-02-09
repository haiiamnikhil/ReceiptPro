from django.urls import path,include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('register/',userRegestrationsView, name = 'register'),
    path('registerform/',userRegisterForm,name = 'registerform'),
    
    path('login/',userLoginView, name = 'login'),
    path('loginform/',userLoginForm, name = 'loginform'),
    
    path('details/',selfUserProfile,name = 'selfuserprofile'),
    path('user/profile/<str:username>/',selfUserProfileView,name='selfuserview'),
    

    path('user/dashboard/',userDashboard,name = 'dashboard'),
    
    path('listusers/',listUsers,name = 'users'),
    path('listuserview/',ListUsersView,name = 'listusers'),
    
    path('isSameUser/',checkUser,name='isSameUser'),
    
    path('emp-profile/<str:username>/',employeeProfileView,name='userProfileView'),
    path('emp-profile/view/<str:username>/',employeeProfile,name='userProfileView'),
    
    path('logout/',logoutUser,name = 'logout')
]