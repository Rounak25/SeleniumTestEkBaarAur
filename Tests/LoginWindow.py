from Demo.POM.Object_Locators.Locators import Locators
class Login():
    # Contrucutor should be made, function pf same class called itself.
    def __init__(self,d):
        self.drive = d
        # self.username_textbox_name = "username" # Locators original (find_element_by_name) name should come.See from Inspect.
        self.password_textbox_name = "password" # Locators original (find_element_by_name) name should come.See from Inspect.
        self.login_button_class_name = "btn.btn-primary.nc-lf-btn" ## Locators original (find_element_by_class_name) name should come.See from Inspect
        # # Upar ke 3 hai = Object...Jo bhi "self" keyword ke sath lage, those are objects.

    def enter_username(self,username): # This all 3 are class ke functions
        self.drive.find_element_by_name(Locators.username_textbox_name).clear()
        self.drive.find_element_by_name(Locators.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.drive.find_element_by_name(self.password_textbox_name).clear()
        self.drive.find_element_by_name(self.password_textbox_name).send_keys(password)

    def login_button(self):
        self.drive.find_element_by_class_name(self.login_button_class_name).click()

