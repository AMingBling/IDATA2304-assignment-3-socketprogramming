from smartTV import SmartTV

tv = SmartTV()

def handle_command(command:str):
    parts = command.strip().split(" ", 1)
    if not parts:
        return "Error: No command received"
    cmd = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    
    if cmd == "1":
        return tv.toggle_power()
    elif cmd == "2":
        return tv.change_channel(1)
    elif cmd == "3":
        return tv.change_channel(-1)
    elif cmd == "4":
        if args.isdigit():
            return tv.set_channel(int(args))
        else:
            return "Error: Invalid channel number"
    elif cmd == "5":
        return tv.list_channels()
    elif cmd == "6":
        return tv.get_status()
    elif cmd == "7":
        return(
            "Supported commands:\n"
            " [1] : Turn TV on/off 📺\n"
            " [2] : Increase channel by one ⬆️\n"
            " [3] : Decrease channel by one ⬇️\n"
            " [4] <number> : Set channel to <number> #️⃣\n"
            " [5] : List available channels 🔢\n"
            " [6] : Get TV status 📊\n"
            " [7] : Show this message ❓\n"
        )
    else:
        return "Error: Unknown command"