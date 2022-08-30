from pytest_html_reporter import attach
import src.domain.modules.loginModule as LoginModule
import config.webdriver as WebDriver

from config.unitTest import Test


class InitialPresentation(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.waitForElementToAppear(loginPage.lblLogInPrompt)

    def tearDown(self):
        if hasattr(self, '_outcome'):
            errors = self._outcome.errors
            attach(data=self.driver.get_screenshot_as_png())
        self.driver.quit()

    # 001 - Initial Presentation
    def test_initialPresentation(self):
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

    # 002 - Forgot Password
    def test_ForgotPassword(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.getElementbyXPath(loginPage.lnkForgotPassword).click()
        assert webdriver.getElementbyXPath(loginPage.lblForgotPassword).text == 'Forgot your password?'

    # 003 - Click Create Account Button
    def test_createAccount(self):
        txtHeader = 'Sloovi Outreach more deals.'
        txtFooter = 'By signing up, you agree to our Terms of Service and Privacy Notice.This page is\nprotected by reCAPTCHA and the Google Privacy Policyand Terms of Service apply.'
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.getElementbyXPath(loginPage.btnCreateAccount).click()
        assert webdriver.getElementbyXPath(loginPage.lblCreateAccountHeader).text == txtHeader
        assert webdriver.getElementbyXPath(loginPage.lblCreateAccountFooter).text == txtFooter

    # 004 - Submit With Incorrect Email Address
    def test_submitIncorrectEmail(self):
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

    # 005- Submit With Incorrect Password
    def test_submitIncorrectPassword(self):
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

    # 006 - Log In To Dashboard
    def test_submitCorrectCredentials(self):
        webdriver = WebDriver.WebDriver(self.driver)
        loginPage = LoginModule.LoginPage(self.driver)

        webdriver.getElementbyXPath(loginPage.inpUsername).send_keys('smithwills1989@gmail.com')
        webdriver.getElementbyXPath(loginPage.inpPassword).send_keys('12345678')
        webdriver.getElementbyXPath(loginPage.btnSignIn).click()
        webdriver.waitForElementToAppear(loginPage.lblUserNameOnDashboard)
