from django.db import models

class Resume(models.Model):
    uploaded_file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
