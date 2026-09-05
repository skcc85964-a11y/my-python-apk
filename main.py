from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical", padding=30, spacing=20
        )

        self.label = Label(
            text="Mera pehla Python APK",
            font_size="24sp"
        )

        button = Button(
            text="Mujhe dabao",
            font_size="22sp"
        )
        button.bind(on_press=self.change_text)

        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def change_text(self, instance):
        self.label.text = "Button dabaya gaya!"

MyApp().run()
