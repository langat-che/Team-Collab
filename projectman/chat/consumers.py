import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message}))
        
        
 
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.roomGroupName = "group_chat_gfg"
#         await self.channel_layer.group_add(
#             self.roomGroupName ,
#             self.channel_name
#         )
#         await self.accept()
#     async def disconnect(self , close_code):
#         await self.channel_layer.group_discard(
#             self.roomGroupName , 
#             self.channel_layer 
#         )
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         username = text_data_json["username"]
#         await self.channel_layer.group_send(
#             self.roomGroupName,{
#                 "type" : "sendMessage" ,
#                 "message" : message , 
#                 "username" : username ,
#             })
#     async def sendMessage(self , event) : 
#         message = event["message"]
#         username = event["username"]
#         await self.send(text_data = json.dumps({"message":message ,"username":username}))
        
        

from channels.db import database_sync_to_async
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))

class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Add the user to the online users list
        await self.add_to_online_users()

        # Notify all connected clients about the updated online users
        await self.send_online_users()

    async def disconnect(self, close_code):
        # Remove the user from the online users list
        await self.remove_from_online_users()

        # Notify all connected clients about the updated online users
        await self.send_online_users()

    async def receive(self, text_data):
        # Handle any additional actions when a message is received
        pass

    @database_sync_to_async
    def add_to_online_users(self):
        # Add the user to the online users list in the database
        # You can use any method to store online users, like a model field or cache
        user = self.scope["user"]
        user.profile.is_online = True
        user.profile.save()

    @database_sync_to_async
    def remove_from_online_users(self):
        # Remove the user from the online users list in the database
        user = self.scope["user"]
        user.profile.is_online = False
        user.profile.save()

    @database_sync_to_async
    def get_online_users(self):
        # Get a list of online users
        online_users = User.objects.filter(profile__is_online=True).values_list("username", flat=True)
        return list(online_users)

    async def send_online_users(self):
        # Send the list of online users to all connected clients
        online_users = await self.get_online_users()
        data = {"type": "user_list", "users": online_users}
        await self.send(text_data=json.dumps(data))