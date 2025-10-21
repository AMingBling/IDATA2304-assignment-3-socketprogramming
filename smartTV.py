class SmartTV:
    def __init__(self):
        self.power = False
        self.channel = 1
        self.available_channels = [1, 2, 3, 4, 5, 6, 7]

    def toggle_power(self):
        self.power = not self.power
        return "TV is now ON" if self.power else "TV is now OFF"

    def change_channel(self, direction: int):
        if not self.power:
            return "Error: TV is OFF"
        current_index = self.available_channels.index(self.channel)
        new_index = current_index + direction
        if new_index < 0 or new_index >= len(self.available_channels):
            return "Error: No more channels in this direction"
        self.channel = self.available_channels[new_index]
        return f"Channel changed to {self.channel}"

    def set_channel(self, channel: int):
        if not self.power:
            return "Error: TV is OFF"
        if channel not in self.available_channels:
            return "Error: Invalid channel number"
        self.channel = channel
        return f"Channel set to {self.channel}"

    def get_status(self):
        power_status = "ON" if self.power else "OFF"
        channel_status = self.channel if self.power else "N/A"
        return f"TV is {power_status}, Active channel: {channel_status}"

    def list_channels(self):
        return "Available channels: " + ", ".join(map(str, self.available_channels))