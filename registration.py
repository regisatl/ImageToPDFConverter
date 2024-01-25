import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RegistrationApp(App):
      def build(self):
            self.title = "Registration Formulaire"
            layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
            
            head_label = Label(text="Python User Registration App", font_size=26, bold=True, height=40)
            
            name_label = Label(text="Name", font_size=18)
            email_label = Label(text="Email", font_size=18)
            password_label = Label(text="Password", font_size=18)
            confirm_password_label = Label(text="Confirm Password", font_size=18)
            
            layout.add_widget(head_label)
            layout.add_widget(name_label)
            layout.add_widget(email_label)
            layout.add_widget(password_label)
            layout.add_widget(confirm_password_label)
            
            return layout

if __name__ == '__main__':
      RegistrationApp().run()