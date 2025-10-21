tv_state = {"power": False, "channel": 1}
def handle_command(command:str):
    parts = command.strip().split(" ", 1)
    if not parts:
        return "Error: No command received"
    cmd = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    
    if cmd == "1":
        return toggle_power()
    elif cmd == "2":
        return change_channel(1)
    elif cmd == "3":
        return change_channel(-1)
    elif cmd == "4":
        if args.isdigit():
            return set_channel(int(args))
        else:
            return "Error: Invalid channel number"
    elif cmd == "5":
        return get_status()
    elif cmd == "6":
        return(
            "Supported commands:\n"
            " [1] : Turn TV on/off 📺\n"
            " [2] : Increase channel by one ⬆️\n"
            " [3] : Decrease channel by one ⬇️\n"
            " [4] <number> : Set channel to <number> #️⃣\n"
            " [5] : Get TV status 📊\n"
            " [6] : Show this message ❓\n"
        )
    else:
        return "Error: Unknown command"
        
def toggle_power():
    tv_state["power"] = not tv_state["power"]
    return "TV is now ON" if tv_state["power"] else "TV is now OFF"
    
def change_channel(direction: int):
    if not tv_state["power"]:
        return "Error: TV is OFF"
    tv_state["channel"] += direction
    if tv_state["channel"] < 1:
        tv_state["channel"] = 1
    return f"Channel changed to {tv_state['channel']}"

def set_channel(channel: int):
    if not tv_state["power"]:
        return "Error: TV is OFF"
    if channel < 1:
        return "Error: Invalid channel number"
    tv_state["channel"] = channel
    return f"Channel set to {tv_state['channel']}"

def get_status():
    power_status = "ON" if tv_state["power"] else "OFF"
    channel_status = tv_state["channel"] if tv_state["power"] else "N/A"
    return f"TV is {power_status}, Active channel: {channel_status}"
