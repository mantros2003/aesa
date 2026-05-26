from cmd_router.router import Feature

NOTE_CMDS = ["note-add", "note-delete", "note-view"]

def note_add_info(cmd: str):
    cmd = cmd.strip()
    if cmd.startswith("note-add"):
        if len(cmd) > 8 and cmd[8] in [" ", ":"]:
            title = cmd[9:].strip()
            return f"Add note with title \"{title}\""
        elif len(cmd) == 8:
            return f"Add note with title \"\""

    return None
