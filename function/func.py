import logging
from cloudevents.http import CloudEvent

def new():
    return Function()

class Function:
    async def handle(self, scope, receive, send):
        logging.info("Request received")
        event = scope["event"]

        # Process RabbitMQ message (inline)
        data = event.data
        logging.info(f"RabbitMQ message: {data}")

        # Create a response CloudEvent
        response = CloudEvent({
            "type": "dev.knative.function.response",
            "source": "https://knative.dev/python-function-response",
            "id": f"response-{event.get('id', 'unknown')}"
        })
        response.data = {"status": "processed"}

        # Send CloudEvent response
        await send(response)