# psscraper - A web scrapper library for https://powerschool.nlmusd.k12.ca.us/
# Copyright (C) 2021 Diego Contreras
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.firefox.webelement import FirefoxWebElement
import os

class PowerschoolBrowser():
    """
        Selenium wrapper for https://powerschool.nlmusd.k12.ca.us/ for
        scrapping. Gives functionality for logging in, viewing classes and
        different pages, and getting page source.
    """

    def __init__(self, debug : bool = False, headless : bool = False,Link='https://powerschool.nlmusd.k12.ca.us/'):
        options = webdriver.FirefoxOptions()

        if headless:
            options.set_headless()
            
        self.browser = webdriver.Firefox(executable_path="./geckodriver", firefox_options=options)
        self.browser.implicitly_wait(5)
        
        self.website = Link
        self.loginDir = "public/home.html"
        self.homeDir = "guardian/home.html"
        self.debug = debug

    def _print(self, msg : str):
        """
            Print if self.debug is True; For debug purposes.
        """
        if self.debug:
            print("{0}: {1}".format(os.path.basename(__file__), msg))

    def searchDir(self, directory : str):
        """
            Navigaes to a directory from https://powerschool.nlmusd.k12.ca.us/.
            The parameter should not start with a forwardslash. e.x.
            "public/home.html"
        """

        website = self.website + directory
        self._print("Going to {0}".format(website))
        self.browser.get(website)

    def loggedIn(self) -> bool:
        """
            Returns whether or not the browser is currently logged in.
        """
        self._print("Checking if logged in...")
        try:
            # This element only exists in logged in pages.
            self.browser.find_element_by_id('parentPageTemp')
            self._print("Logged In!")
            return True
        except NoSuchElementException:
            self._print("Not logged in.")
            return False

    def getPageSource(self) -> str:
        """
            If logged in, return the source of the currently loaded page. Else,
            return None.
        """
        if self.loggedIn():
            return self.browser.page_source

        return None

    def login(self, username : str, password : str) -> bool:
        """
            Logs into a powerschool account given a username and password.
            Returns true if log in was successful.

            NOTE: Username and password are space sensitive, meaning that a
            space or newline character before or after either the username or
            password will not allow you to log in.
        """

        self.searchDir(self.loginDir)
        self._print("Logging in as USER:{0} with PASS:{1}".format(username, password))
       
        self._print("Entering account info...")
        accountField = self.browser.find_element_by_id('fieldAccount')
        accountField.send_keys(username)

        self._print("Entering password...")
        passwordField = self.browser.find_element_by_id('fieldPassword')
        passwordField.send_keys(password)

        self._print("Clicking submit...")
        submitButton = self.browser.find_element_by_id('btn-enter-sign-in')
        submitButton.click()

        return self.loggedIn()

    def close(self):
        """ 
            Closes the browser.
        """

        self._print("Closing browser...")
        self.browser.close()






