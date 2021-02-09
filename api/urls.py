from django.urls import path,include
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('register/',userRegestrationsView, name = 'register'),
    path('registerform/',registerUser,name = 'registerform'),
    path('login/',userLogin, name = 'login'),
    path('details/',userDetails,name = 'details'),
    path('user/dashboard/',userDashboard,name = 'dashboard'),
    path('user/profile/<str:username>/',userProfile,name='profile'),
    path('user/profile/user/',specificUser,name='userprofile'),
    path('logout/',logoutUser,name = 'logout'),
    path('listusers/',listUsers,name = 'users'),
    path('listuserview/',ListUsersView,name = 'listusers'),
    path('isSameUser/',checkUser,name='isSameUser'),
    path('emp-profile/<str:username>/',employeeprofile,name='userProfileView'),
    path('emp-profile/view/<str:username>/',employeeprofiledetails,name='userProfileView')
]