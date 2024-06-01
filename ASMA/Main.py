import json
import pyrebase
import requests
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.app import MDApp
import firebase_admin
from firebase_admin import credentials
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDTextButton
import Functions as df


Window.size = (350,580)

global screen

#cred = credentials.Certificate("serviceAccountKey.json")
#firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://asma-85af3-default-rtdb.firebaseio.com/'
#})


class AboutUsScreen(Screen):
    def AboutUsScreen(self, *args):
        AboutUsScreen(self, *args)
      
class PredictScreen(Screen):
    def PredictScreen(self, *args):
      PredictScreen(self, *args)

class HomeScreen(Screen):
   def HomeScreen(self,*args):
      HomeScreen(self, *args)

screen = ScreenManager()

screen.add_widget(AboutUsScreen(name='aboutUs'))
screen.add_widget(PredictScreen(name='predict'))
screen.add_widget(HomeScreen(name='home'))

class ASMA(MDApp):

  def build(self):
    kv = Builder.load_file("telas.kv")
    screen = kv
    return screen 


ASMA().run()