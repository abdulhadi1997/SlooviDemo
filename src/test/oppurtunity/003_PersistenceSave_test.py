import time

import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LogInModule
import src.domain.modules.opportunityModule as OpportunityModule

from src.domain.unitTest import Test


# 003 - Persistence Save Opportunity
class PersistenceSaveOpportunity(Test):

    statusPrimary = 'boost'
    statusSecondary = 'bads'
    date = '09/30/2022'
    confidenceLevel = '95'
    value = '300'
    valueSegment = 'Monthly'
    contact = 'Saravanan'
    user = 'Sundar Pichai'
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

    def tearDown(self): self.driver.quit()

    def runTest(self):
        webdriver = WebDriver.WebDriver(self.driver)
        opportunity = OpportunityModule.OpportunityModule(self.driver)

        opportunity.setStatus(self.statusPrimary, self.statusSecondary)
        opportunity.setEstimatedClose(self.date)
        opportunity.setConfidence(self.confidenceLevel)
        opportunity.setValue(self.value, self.valueSegment)
        opportunity.setContact(self.contact)
        opportunity.setUser(self.user)
        opportunity.setNote(self.note)
        webdriver.getElementbyXPath(opportunity.btnSave).click()

        assert webdriver.getElementText(opportunity.lblOpportunityName) == '$' + self.value + ' ' + self.valueSegment
        assert webdriver.getElementText(opportunity.lblOpportunityStatus) == self.statusPrimary.upper() + ': ' + self.statusSecondary.upper()
        assert webdriver.getElementText(opportunity.lblOpportunityContact) == self.contact
        assert webdriver.getElementText(opportunity.lblOpportunityNote) == self.note
