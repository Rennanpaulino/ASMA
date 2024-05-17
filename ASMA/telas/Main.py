from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Carregar os arquivos .kv

Builder.load_file('home.kv')
Builder.load_file('prev.kv')
Builder.load_file('sobre.kv')


class Home(Screen):
    pass

class Prev(Screen):
    pass

class Sobre(Screen):
    pass


class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        sm.add_widget(Prev(name='prev'))
        sm.add_widget(Sobre(name='sobre'))
        return sm
    

Main().run()