from django.urls import path
from .views import (
    EmployeeLoginView, ManagerLoginView,
    LogoutView,
    UserDetailView, UserLeaveDaysView,
)

urlpatterns = [
    path('employee-login/', EmployeeLoginView.as_view(), name='employee_login'),
    path('manager-login/' , ManagerLoginView.as_view() , name='manager_login'),
    path('logout/'        , LogoutView.as_view()       , name='logout'),
    path('me/'            , UserDetailView.as_view()   , name='user_detail'),
    path('leave-days/'    , UserLeaveDaysView.as_view(), name='user_leave'),  
]
