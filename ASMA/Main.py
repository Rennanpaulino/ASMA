import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Main(App):
    def build(self):
        return Home()
    

class Home(BoxLayout):
    pass
if __name__ == '__Main__':
    Home().run()