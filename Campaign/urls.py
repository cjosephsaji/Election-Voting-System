from django.urls import path
from . import views
import uuid

urlpatterns = [
	path('', views.admission_number, name='admission-number-page'),
	path(f'{uuid.uuid1()}/<int:student_code>', views.election_page, name='voting-page'),
]