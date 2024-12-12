from selenium.webdriver.common.action_chains import ActionChains
from SeleniumLibrary import SeleniumLibrary

class customkeywords(SeleniumLibrary):
    def context_click(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self._current_browser())
        actions.context_click(element).perform()
