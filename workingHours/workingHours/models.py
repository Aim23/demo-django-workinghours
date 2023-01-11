from django.db import models

class WorkingHours(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def working_duration(self):
        return self.end_time - self.start_time