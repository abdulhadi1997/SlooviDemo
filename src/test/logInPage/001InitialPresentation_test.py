import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LoginModule

from src.domain.unitTest import Test


# 001 - Initial Presentation
class InitialPresentation(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.waitForElementToAppear(loginPage.lblLogInPrompt)

    def tearDown(self): self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.isDisplayed(loginPage.btnCreateAccount)
        webdriver.isDisplayed(loginPage.btnSignIn)
        webdriver.isDisplayed(loginPage.inpEmail)
        webdriver.isDisplayed(loginPage.inpPassword)
        webdriver.isDisplayed(loginPage.lblEmail)
        webdriver.isDisplayed(loginPage.lblLogInPrompt)
        webdriver.isDisplayed(loginPage.lblPassword)
        webdriver.isDisplayed(loginPage.lnkForgotPassword)



