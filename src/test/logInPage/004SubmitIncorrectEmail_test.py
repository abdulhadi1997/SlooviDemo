import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LoginModule
from src.domain.unitTest import Test


# 004 - Submit With Incorrect Email Address
class SubmitIncorrectEmail(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.waitForElementToAppear(loginPage.lblLogInPrompt)

    def tearDown(self): self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.getElementbyXPath(loginPage.btnSignIn).click()
        errorMessage = webdriver.getElementbyXPath(loginPage.inpUsername).get_attribute("validationMessage")
        assert errorMessage == "Please fill in this field."

        webdriver.getElementbyXPath(loginPage.inpUsername).send_keys('smithwills1989')
        webdriver.getElementbyXPath(loginPage.btnSignIn).click()
        errorMessage = webdriver.getElementbyXPath(loginPage.inpUsername).get_attribute("validationMessage")
        assert errorMessage == "Please include an '@' in the email address. 'smithwills1989' is missing an '@'."

        webdriver.getElementbyXPath(loginPage.inpUsername).clear()
        webdriver.getElementbyXPath(loginPage.inpUsername).send_keys('smithwills1989@')
        webdriver.getElementbyXPath(loginPage.btnSignIn).click()
        errorMessage = webdriver.getElementbyXPath(loginPage.inpUsername).get_attribute("validationMessage")
        assert errorMessage == "Please enter a part following '@'. 'smithwills1989@' is incomplete."




