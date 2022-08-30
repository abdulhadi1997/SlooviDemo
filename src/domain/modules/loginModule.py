import config.webdriver as WebDriver


class LoginPage:
    btnCreateAccount = '//a[@class="btn"]'
    btnSignIn = '//button[@class="btn btn-primary"]'
    inpEmail = '//input[@type="email"]'
    inpPassword = '//input[@type="password"]'
    lblEmail = '//span[text()="Email Address"]'
    lblLogInPrompt = '//h2[text()="Please log in to your account"]'
    lblPassword = '//span[text()="Password"]'
    lnkForgotPassword = '//a[@href="/forgot"]'
    inpUsername = '//input[@type="email"]'
    lblUserNameOnDashboard = '//span[@class="OrganizationDropdown_organizationName"]'
    lblForgotPassword = '//h2[@class="Login__title"]'
    lblCreateAccountHeader = '//h2[@class="Login__title"]'
    lblCreateAccountFooter = '//div[@class="terms"]'
    lblValidationError = '//div[@class="Message-danger alert alert-block alert-danger Message--withMargin"]'

    def __init__(self, driver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver

    def logIn(self):
        webdriver = WebDriver.WebDriver(self.driver)

        webdriver.waitForElementToAppear(self.lblLogInPrompt)
        webdriver.getElementbyXPath(self.inpUsername).send_keys('smithwills1989@gmail.com')
        webdriver.getElementbyXPath(self.inpPassword).send_keys('12345678')
        webdriver.getElementbyXPath(self.btnSignIn).click()
        webdriver.waitForElementToAppear(self.lblUserNameOnDashboard)
