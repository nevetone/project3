from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import ChatMessages
import pytz
import time
from datetime import datetime


class Chat(WebsocketConsumer):

    def connect(self):
        self.person_name=self.scope['url_route']['kwargs']['person_name']
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name="chat_%s" % self.room_name
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        
    def disconnect(self, code):

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        FORMAT='%Y-%m-%dT%H:%M:%S'
        date = datetime.strptime(time.strftime(FORMAT, time.localtime()),FORMAT)
        

        async_to_sync(self.channel_layer.group_send)(
            
            self.room_group_name,
            {
                'type':'chat_message',
                'message':"( <span style='color:gold;'>"+str(date)+"</span> )  <span class='righteous'>"+self.person_name+"</span> : <br> <div class='border-top border-light'>"+message+"</div>"
            }
        )
        
        correkt_message = "( <span style='color:gold;'>"+str(date)+"</span> )  <span class='righteous'>"+self.person_name+"</span> : <br> <div class='border-top border-light'>"+message+"</div>"
        x = ChatMessages(nickname=self.person_name, message=correkt_message, room_name=self.room_name)
        x.save()
        
        
    def chat_message(self,event):
        message = event['message']
        
        self.send(text_data=json.dumps({
            'message':message
        }))