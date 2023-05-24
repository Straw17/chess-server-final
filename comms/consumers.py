import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.roomGroupName = "group_chat_gfg"
		await self.channel_layer.group_add(
			self.roomGroupName,
			self.channel_name
		)
		await self.accept()
		
	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.roomGroupName,
			self.channel_name
		)
	
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		playerID = text_data_json["playerID"]
		mirror = text_data_json["mirror"]
		wTurn = text_data_json["wTurn"]
		newBoard = text_data_json["newBoard"]
		wSidebar = text_data_json["wSidebar"]
		bSidebar = text_data_json["bSidebar"]
		await self.channel_layer.group_send(
			self.roomGroupName,{
				"type" : "sendMessage",
				"playerID" : playerID,
				"mirror" : mirror,
				"wTurn" : wTurn,
				"newBoard" : newBoard,
				"wSidebar" : wSidebar,
				"bSidebar" : bSidebar
			})
		
	async def sendMessage(self, event):
		playerID = event["playerID"]
		mirror = event["mirror"]
		wTurn = event["wTurn"]
		newBoard = event["newBoard"]
		wSidebar = event["wSidebar"]
		bSidebar = event["bSidebar"]
		await self.send(text_data = json.dumps({
			"type" : "sendMessage",
			"playerID" : playerID,
			"mirror" : mirror,
			"wTurn" : wTurn,
			"newBoard" : newBoard,
			"wSidebar" : wSidebar,
			"bSidebar" : bSidebar
		}))
