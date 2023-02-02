class Locators():

    # Locators mein hum sabhi web pages(means sabhi alag alag classes) ke objects ko ek sath rakh sakte hai. for better use.

    # Login Window Locators
    username_textbox_name = "username"  # Locators original (find_element_by_name) name should come.See from Inspect.
    password_textbox_name = "password"  # Locators original (find_element_by_name) name should come.See from Inspect.
    login_button_class_name = "btn.btn-primary.nc-lf-btn"  ## Locators original (find_element_by_class_name) name should come.See from Inspect
    # Upar ke 3 hai = Object...Jo bhi "self" keyword ke sath lage, those are objects.

    # Home Page Locators
    profile_button_click = "svg-icon.profile-update-icon"
    logout_button = "svg-icon.mx-auto.log-out-icon.mb-2"
    confirm_log_out_class_name = "btn.btn-secondary.mb-3"
