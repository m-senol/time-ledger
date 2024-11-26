from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    work_duration = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['id', 'date', 'check_in', 'check_out', 'work_duration']

    def get_work_duration(self, obj):
        return obj.calculate_work_duration()
    
    def get_late_duration(self, obj):
        return obj.late_duration
    
    def create(self, validated_data):
        user = self.context['request'].user
        return Attendance.objects.create(user=user, **validated_data)
