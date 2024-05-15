from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Main(App):
    def build(self):
        return Home()
    

class Home(BoxLayout):
    pass

Main().run()