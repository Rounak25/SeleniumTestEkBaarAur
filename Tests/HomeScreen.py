class HomePage():

    def __init__(self,driver):
        self.d = driver
        self.profile_button_click = "svg-icon.profile-update-icon"
        self.logout_button = "svg-icon.mx-auto.log-out-icon.mb-2"
        self.confirm_log_out_class_name = "btn.btn-secondary.mb-3"

    def profile_click(self):
        self.d.find_element_by_class_name(self.profile_button_click).click()

    def logout(self):
        self.d.find_element_by_class_name(self.logout_button).click()

    def confirm_logout(self):
        self.d.find_element_by_class_name(self.confirm_log_out_class_name).click()

