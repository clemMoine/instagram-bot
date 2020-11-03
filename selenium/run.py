#!/usr/bin/env python3

from time import sleep
from selenium import webdriver

from pages.landing import LandingPage 

# Open the web browser
browser = webdriver.Firefox()
browser.implicitly_wait(5)

# Go to landing page of Instagram
landing_page = LandingPage(browser)

# Consent cookies policy
landing_page.consent_cookies_policy()

# Login the user and navigate to home page
home_page = landing_page.login("USERNAME", "PASSWORD")

# Navigate to profile
profile_page = home_page.navigate_to_profile()

# Open the last publication on the profile
last_publication_popin = profile_page.open_last_publication()