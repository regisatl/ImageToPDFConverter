import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class RegistrationApp(App):
      def build(self):
            self.title = "Registration Formulaire"
            layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
            
            head_label = Label(text="PYTHON USER REGISTRATION APP", font_size=26, bold=True, height=40)
            
            name_label = Label(text="Name", font_size=18)
            self.name_input = TextInput(multiline=False, font_size=18)
            
            email_label = Label(text="Email", font_size=18)
            self.email_input = TextInput(multiline=False, font_size=18)
            
            password_label = Label(text="Password", font_size=18)
            self.password_input = TextInput(multiline=False, font_size=18)
            
            confirm_password_label = Label(text="Confirm Password", font_size=18)
            self.confirm_password_input = TextInput(multiline=False, font_size=18)

            submit_button = Button(text='Register', font_size=18, on_press=self.register)
            
            layout.add_widget(head_label)
            layout.add_widget(name_label)
            layout.add_widget(self.name_input)
            layout.add_widget(email_label)
            layout.add_widget(self.email_input)
            layout.add_widget(password_label)
            layout.add_widget(self.password_input)
            layout.add_widget(confirm_password_label)
            layout.add_widget(self.confirm_password_input)
            layout.add_widget(submit_button)
            
            return layout
      
      def register(self, instance):
            name = self.name_input.text
            email = self.email_input.text
            password = self.password_input.text
            confirm_password = self.confirm_password_input.text
            
            if name == "":
                  self.name_input.text = "Name is required"
            elif email == "":
                  self.email_input.text = "Email is required"
            elif password == "":
                  self.password_input.text = "Password is required"
            elif confirm_password == "":
                  self.confirm_password_input.text = "Confirm Password is required"
            elif password!= confirm_password:
                  self.confirm_password_input.text = "Passwords do not match"
            else:
                  self.name_input.text = ""
                  self.email_input.text = ""
                  self.password_input.text = ""
                  self.confirm_password_input.text = ""

if __name__ == '__main__':
      RegistrationApp().run()