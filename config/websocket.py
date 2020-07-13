from one_crm.chatbot.views import get_bot_response


async def websocket_application(scope, receive, send):
    while True:
        event = await receive()

        if event["type"] == "websocket.connect":
            await send({"type": "websocket.accept"})

        if event["type"] == "websocket.disconnect":
            break

        if event["type"] == "websocket.receive":
            user_data = event["text"]
            answer = await get_bot_response(user_data)
            await send({"type": "websocket.send", "text": str(answer)})
