import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LogInModule
import src.domain.modules.opportunityModule as OpportunityModule

from src.domain.unitTest import Test


# 001 - Initial Presentation
class InitialPresentation(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        logIn = LogInModule.LoginPage(self.driver)
        opportunity = OpportunityModule.OpportunityModule(self.driver)

        logIn.logIn()
        webdriver.driver.get('https://stage.outreach.sloovi.com/lead/lead_7e0ce02cc9854ceeb61ea58bbae3f2b6')
        webdriver.waitForElementToAppear(opportunity.lblOpportunityHeader)
        webdriver.getElementbyXPath(opportunity.btnAddOpportunity).click()
        webdriver.scrollTo(opportunity.btnSave)

    def tearDown(self): self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        opportunity = OpportunityModule.OpportunityModule(self.driver)

        assert webdriver.getElementText(opportunity.lblOpportunityHeader) == 'Opportunities'
        assert webdriver.getElementText(opportunity.lblStatus) == 'Status'
        assert webdriver.getElementText(opportunity.lblEstimatedClose) == 'Estimated Close'
        assert webdriver.getElementText(opportunity.lblConfidence) == 'Confidence'
        assert webdriver.getElementText(opportunity.lblValue) == 'Value'
        assert webdriver.getElementText(opportunity.lblContact) == 'Contact'
        assert webdriver.getElementText(opportunity.lblUser) == 'User'
        assert webdriver.getElementText(opportunity.lblNotes) == 'Notes'
        webdriver.isDisplayed(opportunity.inpStatus)
        webdriver.isDisplayed(opportunity.inpEstimatedClose)
        webdriver.isDisplayed(opportunity.scrollerConfidence)
        webdriver.isDisplayed(opportunity.inpValue)
        webdriver.isDisplayed(opportunity.edpValue)
        webdriver.isDisplayed(opportunity.edpContact)
        webdriver.isDisplayed(opportunity.inpUser)
        webdriver.isDisplayed(opportunity.inpNote)


