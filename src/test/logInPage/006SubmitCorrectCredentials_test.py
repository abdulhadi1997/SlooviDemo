import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LoginModule
from src.domain.unitTest import Test


# 006 - Log In To Dashboard
class Test_LogInToDashboard(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.waitForElementToAppear(loginPage.lblLogInPrompt)

    def tearDown(self): self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.getElementbyXPath(loginPage.inpUsername).send_keys('smithwills1989@gmail.com')
        webdriver.getElementbyXPath(loginPage.inpPassword).send_keys('12345678')
        webdriver.getElementbyXPath(loginPage.btnSignIn).click()
        webdriver.waitForElementToAppear(loginPage.lblUserNameOnDashboard)
