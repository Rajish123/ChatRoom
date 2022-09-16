from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # w+ is saying anything after chat/ is going to be recognized and picked up 
    # w = match a word character i.e, match any word with any length, any upper/lower case character that can be alphabets,digits,0-9,underscore character
    re_path(r'ws/chat/(?P<room_name>\w+)/$',consumers.ChatRoomConsumer.as_asgi())
]