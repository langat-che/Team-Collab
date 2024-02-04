# import os
# from channels.routing import ProtocolTypeRouter
# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         # Just HTTP for now. (We can add other protocols later.)
#     }
# )

# from django.urls import re_path, path
# from . import consumers
# from chat.consumers import ChatConsumer

# websocket_urlpatterns = [
#     re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
#     path("" , ChatConsumer.as_asgi()) ,
# ]

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
# from chat.consumers import ChatConsumer

# application = ProtocolTypeRouter({
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             [
#                 path("ws/users/", ChatConsumer.as_asgi()),
#             ]
#         )
#     ),
# })

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/users/$', consumers.UserConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})