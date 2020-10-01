from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

DynamicLabelsApp().run()