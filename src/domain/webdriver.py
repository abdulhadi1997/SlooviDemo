from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class WebDriver:

    def __init__(self, driver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver

    def getDriver(self):
        return self.driver

    def waitForElementToHaveText(self, elementLocator="", expectedText=''):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, elementLocator), expectedText))

    def waitForElementToBeClickable(self, elementLocator=""):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, elementLocator)))

    def waitForElementToAppear(self, elementLocator=""):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, elementLocator)))

    def waitForElementToDisappear(self, elementLocator=""):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, elementLocator)))

    def isDisplayed(self, elementLocator=""):
        return self.driver.find_element(By.XPATH, elementLocator)

    def isNotDisplayed(self, elementLocator=""):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, elementLocator)))

    def getElementText(self, elementLocator=""):
        return self.driver.find_element(By.XPATH, elementLocator).text

    def getElementbyXPath(self, elementXPath=""):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, elementXPath)))
        return self.driver.find_element(By.XPATH, elementXPath)

    def getElementbyCSS(self, elementCSS=""):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, elementCSS)))
        return self.driver.find_element(By.CSS_SELECTOR, elementCSS)

    def getElementbyID(self, elementID=""):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, elementID)))
        return self.driver.find_element(By.ID, elementID)

    def clearField(self, elementXPath, iterations):
        for i in range(iterations):
            self.driver.find_element(By.XPATH, elementXPath).send_keys(Keys.BACKSPACE)

    def scrollTo(self, elementXPath):
        element = self.driver.find_element(By.XPATH, elementXPath)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
