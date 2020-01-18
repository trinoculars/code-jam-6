# qpy:kivy

# Kivy Imports
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.theming import ThemeManager
from kivy.app import App


# Project imports
from ui.screens.welcome_screen import WelcomeScreen
from ui.screens.encoder_screen import EncoderScreen
from ui.screens.decoder_screen import DecoderScreen
from util.utility import Utility


class MainBox(FloatLayout):
    def __init__(self, **kwargs):
        super(MainBox, self).__init__()
        self.screens = AnchorLayout(anchor_x='center', anchor_y='center')
        self.util = Utility()
        self.content = ScreenManager()

        # Place screens here
        self.content.add_widget(WelcomeScreen(name='welcome', util=self.util))
        self.content.add_widget(EncoderScreen(name='encode', util=self.util))
        self.content.add_widget(DecoderScreen(name='decode', util=self.util))
        # Place screens here

        self.screens.add_widget(self.content)

        self.add_widget(self.screens)


class MainApp(App):
    # Change APP colors here
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'
    theme_cls.primary_hue = '300'
    theme_cls.accent_palette = 'Gray'
    theme_cls.accent_hue = '800'
    accent_color = [255/255, 64/255, 129/255,1]

    def build(self):
        return MainBox()


if __name__ == "__main__":
    MainApp().run()
