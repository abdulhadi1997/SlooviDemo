import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LoginModule
from src.domain.unitTest import Test


# 002 - Forgot Password
class ForgotPassword(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.waitForElementToAppear(loginPage.lblLogInPrompt)

    def tearDown(self): self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.getElementbyXPath(loginPage.lnkForgotPassword).click()
        assert webdriver.getElementbyXPath(loginPage.lblForgotPassword).text == 'Forgot your password?'




