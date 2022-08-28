import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LoginModule
from src.domain.unitTest import Test


# 005- Submit With Incorrect Password
class SubmitIncorrectPassword(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.waitForElementToAppear(loginPage.lblLogInPrompt)

    def tearDown(self): self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.getElementbyXPath(loginPage.inpUsername).send_keys('smithwills1989@gmail.com')
        webdriver.getElementbyXPath(loginPage.btnSignIn).click()
        errorMessageNoPassword = webdriver.getElementbyXPath(loginPage.inpPassword).get_attribute("validationMessage")
        assert errorMessageNoPassword == "Please fill in this field."

        webdriver.getElementbyXPath(loginPage.inpPassword).send_keys('87654321')
        webdriver.getElementbyXPath(loginPage.btnSignIn).click()

        webdriver.waitForElementToAppear(loginPage.lblValidationError)
        errorMessageIncorrectPassword = webdriver.getElementbyXPath(loginPage.lblValidationError).text
        assert errorMessageIncorrectPassword == "The email address or password was incorrect."
