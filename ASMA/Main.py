import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Home(App):
    def build(self):
        
        # Definindo a interface do usuário
        layout = BoxLayout(orientation='vertical')

        # Adicionando uma label no meio da tela
        label = Label(text='ASMA 1.3', size_hint=(1, 0.5))
        layout.add_widget(label)

        # Adicionando uma barra com três botões na parte inferior
        bottom_bar = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        button1 = Button(text='Configurações', size_hint=(0.33, 0.6))
        button2 = Button(text='Casa', size_hint=(0.33, 0.6))
        button3 = Button(text='Pesquisa', size_hint=(0.33, 0.6))
        bottom_bar.add_widget(button1)
        bottom_bar.add_widget(button2)
        bottom_bar.add_widget(button3)
        layout.add_widget(bottom_bar)

        return layout


if __name__ == '__main__':
    Home().run()