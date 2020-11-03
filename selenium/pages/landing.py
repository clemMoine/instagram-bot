from time import sleep

from pages.home import HomePage

class LandingPage:
    def __init__(self, browser):
        self.browser = browser

        # Navigate to Instagram
        self.browser.get('https://www.instagram.com/')

    def consent_cookies_policy(self):
        # Gather and click the cookies consent button
        cookies_consent = self.browser.find_element_by_css_selector("button.aOOlW.bIiDR")
        cookies_consent.click()

    def login(self, username, password):
        # Gather the login and password input DOM elements
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        # Fill the credentials with the given environnement credentials 
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Gather and click the submit button for login form 
        login_button = self.browser.find_element_by_css_selector("button[type='submit']")
        login_button.click()

        sleep(5)

        # Gather and click the reject button for credentials remembering pop-in
        reject_credentials_remember = self.browser.find_element_by_css_selector("button.sqdOP.yWX7d.y3zKF")
        reject_credentials_remember.click()

        sleep(3)

        return HomePage(self.browser)
