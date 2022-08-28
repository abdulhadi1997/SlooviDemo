import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LogInModule
import src.domain.modules.opportunityModule as OpportunityModule

from src.domain.unitTest import Test


# 002 - Persistence Cancel Opportunity
class PersistenceCancelOpportunity(Test):

    statusPrimary = 'boost'
    statusSecondary = 'bads'
    date = '09/30/2022'
    value = '300'
    valueSegment = 'Monthly'
    contact = 'Saravanan'
    note = 'Testing'

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        logIn = LogInModule.LoginPage(self.driver)
        opportunity = OpportunityModule.OpportunityModule(self.driver)

        logIn.logIn()
        webdriver.driver.get('https://stage.outreach.sloovi.com/lead/lead_7e0ce02cc9854ceeb61ea58bbae3f2b6')
        webdriver.waitForElementToAppear(opportunity.lblOpportunityHeader)
        webdriver.getElementbyXPath(opportunity.btnAddOpportunity).click()
        webdriver.scrollTo(opportunity.btnSave)

    def tearDown(self):
        self.driver.save_screenshot("screenshot" + self.id() + ".png")
        self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        opportunity = OpportunityModule.OpportunityModule(self.driver)

        opportunity.setStatus(self.statusPrimary, self.statusSecondary)
        opportunity.setEstimatedClose(self.date)
        opportunity.setConfidence('95')
        opportunity.setValue(self.value, self.valueSegment)
        opportunity.setContact(self.contact)
        opportunity.setUser('Sundar Pichai')
        opportunity.setNote(self.note)
        webdriver.getElementbyXPath(opportunity.btnCancel).click()

        assert webdriver.isNotDisplayed(opportunity.lblOpportunityName)


