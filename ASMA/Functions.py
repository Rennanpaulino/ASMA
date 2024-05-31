import firebase_admin
import pyrebase 
from kivymd.app import MDApp
from kivymd.uix.button import MDTextButton, MDFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

global firebaseConfig 

def callAboutUs(self, *args):
    MDApp.get_running_app().root.current = 'aboutUs'
