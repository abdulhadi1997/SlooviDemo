import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LoginModule
from src.domain.unitTest import Test


# 003 - Click Create Account Button
class ForgotPassword(Test):
    txtHeader = 'Sloovi Outreach more deals.'
    txtFooter = 'By signing up, you agree to our Terms of Service and Privacy Notice.This page is\nprotected by reCAPTCHA and the Google Privacy Policyand Terms of Service apply.'

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.waitForElementToAppear(loginPage.lblLogInPrompt)

    def tearDown(self): self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.getElementbyXPath(loginPage.btnCreateAccount).click()
        assert webdriver.getElementbyXPath(loginPage.lblCreateAccountHeader).text == self.txtHeader
        assert webdriver.getElementbyXPath(loginPage.lblCreateAccountFooter).text == self.txtFooter





