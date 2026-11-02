#Build
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):
        return MDLabel(text="Meri Pehli APK!", halign="center")

MyApp().run()
