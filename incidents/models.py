from django.db import models

class Incident(models.Model):
    SEVERITY_CHOICES = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    )

    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )


    incident_id = models.CharField(max_length=100)
    incident_name = models.CharField(max_length=100)
    incident_description = models.CharField(max_length=100)
    incident_status = models.CharField(max_length=100)
    incident_date = models.DateTimeField('date published')