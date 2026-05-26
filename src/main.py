from textual.app import App
from typing import Optional
import os
import json
from datetime import datetime
from datacalsses import dataclass
from enum import Enum
from screens.signup_screen import SignupScreen
from screens.welcome_screen import MainScreen

DATA_DIR = ".aesa"
USER_DATA_FILE = os.path.join(DATA_DIR, "udata.josn")

class AppMode(Enum):
    LOGIN,
    WELCOME

@dataclass
class AppState:
    user: Optional[str],
    username: Optional[str],
    created: Optional[str],
    mode: AppMode

class MyApp(App):
    def __init__(self):
        super().__init__()

        self.udata = None
        self.state = AppState(None, None, None, AppState.LOGIN)

    async def on_mount(self):
        self.run_worker(self._handle_startup())

    async def _handle_startup(self):
        udata = self._load_data()
        if not udata:
            usrnm, pswd = await self._create_new_user()
            udata = {
                "username": usrnm,
                "password": pswd,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    
            if not (os.path.exists(DATA_DIR) and os.path.isdir(DATA_DIR)):
                os.makedirs(DATA_DIR, exist_ok=True)
    
            with open(USER_DATA_FILE, "w") as udata_file:
                json.dump(udata, udata_file, indent=4)

        self.udata = udata
        self.state.username = udata["username"]
        self.state.created = udata["created"]
        self.push_screen(MainScreen())

    async def _create_new_user(self):
        usernm, passwd = await self.push_screen_wait(SignupScreen())

        return usernm, passwd
    
    def _load_data(self):
        if not os.path.exists(DATA_DIR):
            return False
        if not (os.path.exists(USER_DATA_FILE) and os.path.isfile(USER_DATA_FILE)):
            return False
    
        with open(USER_DATA_FILE, "r") as udata_file:
            udata = json.load(udata_file)
            return udata



if __name__ == "__main__":
    app = MyApp()
    app.run()
