from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
import random
Builder.load_file('hb.kv')

class Anasayfa(Screen):
    def giris(self, kadiText, sifreText):
        app = App.get_running_app()
        app.kullanici = kadiText
        app.sifre = sifreText
        if app.kullanici == "admin" and app.sifre == "admin":
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'giris'
        else:
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'hatali'
            

        app.config.read(app.get_application_config())
        app.config.write()

    def resetForm(self):
        self.ids['kadi'].text = ""
        self.ids['sifre'].text = ""

class giris(Screen):
    def kelime(self, *args):

        label = self.ids['degisken']
        
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'anasayfa'
        self.manager.get_screen('anasayfa').resetForm()

class hatali(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'anasayfa'
        self.manager.get_screen('anasayfa').resetForm()



sm = ScreenManager()
sm.add_widget(Anasayfa(name='anasayfa'))
sm.add_widget(giris(name='giris'))
sm.add_widget(hatali(name='hatali'))

class TestApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        return sm 



if __name__ == '__main__':
    TestApp().run()
