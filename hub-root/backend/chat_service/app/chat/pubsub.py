
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# channel_layer = get_channel_layer()

# # Subscribe to the Redis channel
# async def subscribe_to_channel():
#     await channel_layer.group_add('chat', 'websocket.channel')


# # WebSocket consumer
# async def ws_connect(message):
#     await subscribe_to_channel()
#     await message.reply_channel.send({'accept': True})


# Example: In another Django application that subscribes to the Redis channel

# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# channel_layer = get_channel_layer()

# # Subscribe to the Redis channel with a specific room ID
# async def subscribe_to_channel(room_id):
#     channel_name = f'chat_{room_id}'  # Use a channel name based on the room ID
#     await channel_layer.group_add(channel_name, 'websocket.channel')

# # WebSocket consumer
# async def ws_connect(message):
#     room_id = message['path'].split('/')[-1]  # Extract room ID from the URL
#     await subscribe_to_channel(room_id)
#     await message.reply_channel.send({'accept': True})

# async def ws_disconnect(message):
#     room_id = message['path'].split('/')[-1]  # Extract room ID from the URL
#     channel_name = f'chat_{room_id}'
#     await message.channel_layer.group_discard(channel_name, 'websocket.channel')

# # Handle room creation event
# async def room_created(event):
#     room_name = event['room_name']
#     # Handle the event, e.g., update UI, join the new room, etc.
