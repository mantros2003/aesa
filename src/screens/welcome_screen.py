from textual.screen import Screen
from textual.widgets import Label

class MainScreen(Screen):

    def compose(self):
        username = self.app.udata["username"]
        date_joined = self.app.udata["created"]
        output_text = f"Welcome {username}" + '\n' + f"Account created on {date_joined}"
        yield Label(output_text)
