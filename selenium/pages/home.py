from time import sleep

from pages.profile import ProfilePage

class HomePage:
    def __init__(self, browser):
        self.browser = browser

        # Gather and click the reject button DOM element from the notification subscription pop-in
        reject_notification_subscription = self.browser.find_element_by_css_selector("button.aOOlW.HoLwm")
        reject_notification_subscription.click()

    def navigate_to_profile(self):
        # Gather and click the user avatar image DOM element
        user_avatar = self.browser.find_element_by_css_selector("span[role='link']._2dbep.qNELH")
        user_avatar.click()

        # Gather and click the profile link DOM element
        profile_link = self.browser.find_element_by_css_selector("a[href].-qQT3")
        profile_link.click()

        sleep(5)

        return ProfilePage(self.browser)