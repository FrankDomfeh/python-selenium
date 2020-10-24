class LoginPage:
    textbox_username_id = 'Email'
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_link_text = "Logout"

    # Create a Constructor to implement the action methods
    def __init__(self, driver):
        self.driver = driver

    # Creating Action method for the captured elements
    def setUsername(self, username):
        userName = self.driver.find_element_by_id(self.textbox_username_id)
        userName.clear()
        userName.send_keys(username)

    def setPassword(self, password):
        userPassword = self.driver.find_element_by_id(self.textbox_password_id)
        userPassword.clear()
        userPassword.send_keys(password)

    def clickLogin(self):
        loginButton = self.driver.find_element_by_xpath(self.button_login_xpath)
        loginButton.click()

    def clickLogout(self):
        logoutButton = self.driver.find_element_by_link_text(self.link_logout_link_text)
        logoutButton.click()