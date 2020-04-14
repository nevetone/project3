from django.urls import re_path
from main import Chat

websocket_urlpaterns=[
    re_path(r'/chat/(?P<room_name>\w+)/(?P<person_name>\w+)/$', Chat.Chat)
]