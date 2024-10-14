from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window

class DragDropApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Drag and Drop a file or Browse")
        
        # Browse Button
        self.browse_button = Button(text="Browse Files")
        self.browse_button.bind(on_press=self.browse_files)

        # File Chooser (for browsing files)
        self.file_chooser = FileChooserIconView(filters=['*.*'])  # Allow browsing all file types
        self.file_chooser.bind(on_submit=self.on_file_select)
        
        # Add widgets to the layout
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.browse_button)
        self.layout.add_widget(self.file_chooser)

        # Bind drag and drop from OS
        Window.bind(on_dropfile=self.on_file_drop)
        
        return self.layout

    def browse_files(self, instance):
        # Trigger file chooser browsing functionality
        self.file_chooser.open()

    def on_file_select(self, instance, selected_file):
        # This handles file selection from the FileChooser
        if selected_file:
            self.label.text = f"Selected file: {selected_file[0]}"

    def on_file_drop(self, window, file_path):
        # This handles file drag-and-drop from OS
        file_path = file_path.decode('utf-8')  # Decode file path from bytes to string
        self.label.text = f"Dropped file: {file_path}"

if __name__ == '__main__':
    DragDropApp().run()
