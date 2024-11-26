from django.urls import path
from .views import (
    home_page,
    employee_login_page, manager_login_page,
    employee_home_page, manager_home_page,
    leave_form_page, leave_requests_page, employee_used_leaves_page
)

urlpatterns = [
    path(''                          , home_page                , name='home'),
    path('employee-login-page/'      , employee_login_page      , name='employee_login_page'),
    path('manager-login-page/'       , manager_login_page       , name='manager_login_page'),  
    path('employee-home-page/'       , employee_home_page       , name='employee_home_page'),
    path('employee-used-leaves-page/', employee_used_leaves_page, name='employee_used_leaves_page'),
    path('leave-form-page/'          , leave_form_page          , name='leave_form_page'),
    path('leave-requests-page/'      , leave_requests_page      , name='leave_requests_page'),
    path('manager-home-page/'        , manager_home_page        , name='manager_home_page'),
]
