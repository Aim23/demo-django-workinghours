from django import forms
from .models import WorkingHours

class WorkingHoursForm(forms.ModelForm):
    class Meta:
        model = WorkingHours
        fields = ['date', 'start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if end_time <= start_time:
            raise forms.ValidationError("End time must be greater than start time.")
        
        working_duration = end_time - start_time
        if working_duration.total_seconds()/3600 < 7.6:
            self.add_error('start_time', "Working hours must be atleast 7.6 hr daily")
        elif working_duration.total_seconds()/3600 > 10.75:
            self.add_error('start_time', "Working hours exceed 10.75 hr limit")