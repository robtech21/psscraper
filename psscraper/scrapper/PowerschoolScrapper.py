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


from bs4 import BeautifulSoup
import bs4
import os

class PowerschoolScrapper:
    """ 
        Base class for all powerschool scrappers. This gives toggleable debug
        statements and automates HTML parsing.
    """

    def __init__(self, pageSource : str, debug : bool = False):
        self.soup = BeautifulSoup(pageSource, 'html.parser')
        self.debug = debug

    def _print(self, msg : str):
        """
            Prints if self.debug is true.
        """

        if self.debug:
            print(os.path.basename(self._getFileName()) + ": " + msg)

    def _getFileName(self):
        return __file__
