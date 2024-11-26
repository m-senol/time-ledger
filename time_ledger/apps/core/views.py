from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from datetime import datetime
from apps.attendance.models import Attendance

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def employee_login_page(request):
    return render(request, 'employee_login.html')

def manager_login_page(request):
    return render(request, 'manager_login.html')

@login_required
def employee_home_page(request):
    return render(request, 'employee_home.html')

@login_required
def employee_used_leaves_page(request):
    return render(request, 'employee_used_leaves.html')

@login_required
def leave_form_page(request):
    return render(request, 'leave_form.html')

@login_required
def leave_requests_page(request):
    return render(request, 'leave_requests.html')

@login_required
def manager_home_page(request):
    if not request.user.is_manager:
        return redirect('home')
    
    today = datetime.now().date()
    late_arrivals = Attendance.objects.filter(date=today).exclude(late_duration__isnull=True)
    
    context = {
        'late_arrivals': [
            {
                'employee_name': f"{late.user.first_name} {late.user.last_name or late.user.username}",
                'duration': str(late.late_duration) 
            }
            for late in late_arrivals
        ]
    }
    return render(request, 'manager_home.html', context)
