from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from datetime import datetime
from .models import Attendance


@method_decorator(login_required, name='dispatch')
class CheckInView(View):
    def post(self, request):
        today = datetime.now().date()
        attendance, _ = Attendance.objects.get_or_create(user=request.user, date=today)
        
        if attendance.check_in:
            return JsonResponse({"message": "You have already checked in today."}, status=400)
        
        attendance.check_in = datetime.now().time()
        attendance.late_duration = attendance.calculate_late_duration()
        attendance.save()
        
        return JsonResponse({"message": "Check-in successful", "check_in": str(attendance.check_in)}, status=200)


@method_decorator(login_required, name='dispatch')
class CheckOutView(View):
    def post(self, request):
        today = datetime.now().date()

        try:
            attendance = Attendance.objects.get(user=request.user, date=today)
        except Attendance.DoesNotExist:
            return JsonResponse({"message": "You need to check in before checking out."}, status=400)

        if not attendance.check_in:
            return JsonResponse({"message": "You need to check in before checking out."}, status=400)

        if attendance.check_out:
            return JsonResponse({"message": "You have already checked out today."}, status=400)

        attendance.check_out = datetime.now().time()
        attendance.save()

        return JsonResponse({"message": "Check-out successful", "check_out": str(attendance.check_out)}, status=200)
