from textual.screen import Screen
from textual.widgets import Button, Input, Label
from textual.containers import Vertical
from textual import on

class SignupScreen(Screen):

    def compose(self):
        yield Vertical(
            Label("Sign up"),
            Input(placeholder="Username", id="username"),
            Input(password=True, placeholder="Password", id="password"),
            Button("Continue", id="submit"),
        )

    @on(Button.Pressed, "#submit")
    def submit_button(self):
        usernm = self.query_one("#username", Input).value
        passwd = self.query_one("#password", Input).value

        self.dismiss((usernm, passwd))



