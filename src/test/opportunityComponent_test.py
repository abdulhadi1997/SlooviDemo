import src.domain.modules.loginModule as LogInModule
import src.domain.modules.opportunityModule as OpportunityModule
import src.domain.modules.taskModule as TaskModule
import config.webdriver as WebDriver

from config.unitTest import Test
from pytest_html_reporter import attach


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

    def tearDown(self):
        if hasattr(self, '_outcome'):
            errors = self._outcome.errors
            attach(data=self.driver.get_screenshot_as_png())
        self.driver.quit()

    # 001 - Initial Presentation
    def test_initialPresentation(self):
        webdriver = WebDriver.WebDriver(self.driver)
        opportunity = OpportunityModule.OpportunityModule(self.driver)

        webdriver.waitForElementToHaveText(opportunity.lblOpportunityHeader, 'Opportunities')
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

    # 002 - Persistence Cancel Opportunity Component
    def test_persistenceCancel(self):
        webdriver = WebDriver.WebDriver(self.driver)
        task = TaskModule.TaskModule(self.driver)
        taskDescription = Test.randomizeName(self.driver, 'persistenceCancelTest')

        webdriver.clearField(task.inpTaskDescription, 8)
        task.setTaskDescription(taskDescription)
        task.setDate('09/30/2022')
        task.setTime('01:00am')
        task.setAssignUser('Saravanan C')
        webdriver.getElementbyXPath(task.btnCancel).click()
        webdriver.waitForElementToDisappear(task.lblTaskDescription)
        assert webdriver.getElementText(task.lblFirstTaskComponent) != taskDescription

    # 003 - Persistence Save Opportunity     Component
    def test_persistenceSave(self):
        webdriver = WebDriver.WebDriver(self.driver)
        task = TaskModule.TaskModule(self.driver)
        taskDescription = Test.randomizeName(self.driver, 'persistenceSaveTest')

        webdriver.clearField(task.inpTaskDescription, 8)
        task.setTaskDescription(taskDescription)
        task.setDate('09/30/2022')
        task.setTime('01:00am')
        task.setAssignUser('Saravanan C')
        webdriver.getElementbyXPath(task.btnSave).click()
        webdriver.waitForElementToDisappear(task.lblTaskDescription)
        assert webdriver.getElementText(task.lblFirstTaskComponent) == taskDescription
