from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem

KV = '''
ScreenManager:
    LoginScreen:
    DashboardScreen:

<LoginScreen>:
    name: "login"
    MDFloatLayout:
        MDLabel:
            text: "Corporate Login"
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_style: "H5"
            halign: "center"

        MDTextField:
            id: username
            hint_text: "Username"
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            size_hint_x: 0.8

        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size_hint_x: 0.8

        MDRaisedButton:
            text: "Login"
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            on_release: app.login(username.text, password.text)

<DashboardScreen>:
    name: "dashboard"
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Corporate Dashboard"
            left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]

        MDLabel:
            text: "Welcome, Admin!"
            halign: "center"

    MDNavigationLayout:
        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: "vertical"

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                padding: "8dp"

                MDLabel:
                    text: "Menu"
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: "Dashboard"
                            on_release: app.change_screen("dashboard")

                        OneLineListItem:
                            text: "Settings"
                            on_release: app.change_screen("settings")

                        OneLineListItem:
                            text: "Logout"
                            on_release: app.logout()
'''

class LoginScreen(MDScreen):
    pass

class DashboardScreen(MDScreen):
    pass

class CorporateApp(MDApp):
    def build(self):
        self.sm = Builder.load_string(KV)
        return self.sm

    def login(self, username, password):
        if username == "admin" and password == "pass":
            self.sm.current = "dashboard"
        else:
            MDDialog(title="Login Failed", text="Invalid username or password").open()

    def logout(self):
        self.sm.current = "login"

    def change_screen(self, screen_name):
        self.sm.current = screen_name

CorporateApp().run()