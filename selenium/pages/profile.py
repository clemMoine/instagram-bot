from time import sleep

from pages.publication import PublicationPopin

class ProfilePage:
    def __init__(self, browser):
        self.browser = browser

    def open_last_publication(self):
        # Gather and click the last publication DOM element
        last_publication = self.browser.find_element_by_css_selector("article a[href]:first-of-type")
        last_publication.click()

        return PublicationPopinPage(self.browser)