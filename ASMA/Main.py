from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class Home(BoxLayout):
    pass

class Main(App):
    def build(self):
        self.load_kv('home.kv')
        return Home()
    

Main().run()