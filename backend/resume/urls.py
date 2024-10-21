from django.urls import path
from .views import upload_resume, analyze_resume, upload_and_analyze

urlpatterns = [
    path('upload/', upload_resume, name='upload_resume'),
    path('analyze/', analyze_resume, name='analyze_resume'),
    path('upload_and_analyze/', upload_and_analyze, name='upload_and_analyze'),

]