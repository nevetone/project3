from django.urls import path
from . import views

urlpatterns = [
    path('room/<str:room_name>/<str:person_name>', views.SchowChatPage, name="showchatpage")
]
