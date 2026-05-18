from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Input, Label, ListItem, ListView

class CenteredSearchApp(App):
    """An app featuring a perfectly centered search bar."""

    ENABLE_COMMAND_PALETTE = False
    
    BINDINGS = [
        ("q", "quit", "Quit")
    ]

    # Loading the CSS styles from an external string (or separate file)
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        
        # We wrap our search components in a container so we can center it
        with Vertical(id="search-container"):
            yield Label("Search", id="search-label")
            yield Input(placeholder="Type something to search...", id="search-input")
            
            # A hidden list view that we can populate later
            yield ListView(id="search-results")
            
        yield Footer()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Called automatically whenever the user types in the Input field."""
        search_box = event.input
        results_list = self.query_one("#search-results", ListView)
        
        # Clear previous results
        results_list.clear()
        
        # Example logic: If they type something, show a couple dummy results
        if event.value.strip():
            results_list.display = True  # Make sure the list is visible
            results_list.append(ListItem(Label(f"🔍 Result 1 for '{event.value}'")))
            results_list.append(ListItem(Label(f"🔍 Result 2 for '{event.value}'")))
        else:
            # Hide the results box if the search bar is empty
            results_list.display = False

    def on_key(self, event) -> None:
        """Global key event interceptor."""
        # 2. Check if the user pressed the 'down' arrow key
        if event.key == "down":
            # 3. Only jump if the user is currently focusing on the search input
            if self.focused and self.focused.id == "search-input":
                results_list = self.query_one("#search-results", ListView)
                
                # If there are actual results visible, move focus to the list
                if results_list.display and len(results_list.children) > 0:
                    results_list.focus()
                    results_list.index = 0  # Highlight the very first item
                    event.prevent_default()  # Stop the key from doing anything else

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Triggered when the user presses 'Enter' on a selected list item."""
        selected_item = event.item
        self.notify(f"You selected: {selected_item.id}")


if __name__ == "__main__":
    app = CenteredSearchApp()
    app.run()
