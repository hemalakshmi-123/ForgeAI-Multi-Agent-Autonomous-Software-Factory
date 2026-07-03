# forge/communication/event_bus.py

class EventBus:
    def __init__(self, registry):
        self.registry = registry
        self.history = []
        self.listeners = {}

    def subscribe(self, event_type: str, callback):
        """Allows agents or orchestrators to listen for specific system events synchronously."""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)

    def publish(self, event_type: str, message):
        self.history.append(message)
        receiver = self.registry.get(message.receiver)

        if receiver:
            receiver.receive_message(message)
            # Dispatch to any registered functional callbacks
            if event_type in self.listeners:
                for callback in self.listeners[event_type]:
                    callback(message)
        else:
            print(f"[EventBus] Warning: Target Agent '{message.receiver}' not found in registry.")

    def get_history(self):
        return self.history