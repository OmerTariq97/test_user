from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

# Basic SyncConsumer
class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print(self.channel_name)
        print(self.channel_layer)
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": 'kek from server',
        })
    def disconnect(self, close_code):
        print('web socket disconnected1')
        raise StopConsumer()

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('channel layer', self.channel_layer)
        print('channel name', self.channel_name)

        async_to_sync(self.channel_layer.group_add)(
            'friends',
            self.channel_name)

        self.send({
            "type": "websocket.accept",
        })
        print('web socket connected1')

    def websocket_receive(self, event):
        # self.send({
        #     "type": "websocket.send",
        #     "text": 'yo nigg nigg',
        # })
        print('data received from socket1', event['text'])
        async_to_sync(self.channel_layer.group_send)(
            'friends', {
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        self.send({
            "type": "websocket.send",
            "text": event['message']
        })
        print('eventtt', event)


    def disconnect(self, close_code):
        print('web socket disconnected1')
        raise StopConsumer()


class MyASyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        # self.send({
        #     "type": "websocket.accept",
        # })
        print('web socket connected1')

    async def websocket_receive(self, event):
        # self.send({
        #     "type": "websocket.send",
        #     "text": event["text"],
        # })
        print('data received from socket1')


    async def disconnect(self, close_code):
        print('web socket disconnected1', )
        print('channel layer', self.channel_layer)
        print('channel name', self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            'friends',
            self.channel_name)
        raise StopConsumer()