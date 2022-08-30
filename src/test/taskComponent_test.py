import src.domain.modules.loginModule as LogInModule
import src.domain.modules.taskModule as TaskModule
import config.webdriver as WebDriver

from config.unitTest import Test
from pytest_html_reporter import attach


class InitialPresentation(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        logIn = LogInModule.LoginPage(self.driver)
        task = TaskModule.TaskModule(self.driver)

        logIn.logIn()
        webdriver.driver.get('https://stage.outreach.sloovi.com/lead/lead_7e0ce02cc9854ceeb61ea58bbae3f2b6')
        webdriver.waitForElementToAppear(task.lblComponentHeader)
        webdriver.getElementbyXPath(task.btnAddTask).click()

    def tearDown(self):
        if hasattr(self, '_outcome'):
            errors = self._outcome.errors
            attach(data=self.driver.get_screenshot_as_png())
        self.driver.quit()

    # 001 - Initial Presentation
    def test_initialPresentation(self):
        webdriver = WebDriver.WebDriver(self.driver)
        task = TaskModule.TaskModule(self.driver)

        assert webdriver.getElementText(task.lblComponentHeader) == 'Tasks'
        assert webdriver.getElementText(task.lblTaskDescription) == 'Task Description'
        assert webdriver.getElementText(task.lblDate) == 'Date'
        assert webdriver.getElementText(task.lblAssignUser) == 'Assign User'
        webdriver.isDisplayed(task.inpTaskDescription)
        webdriver.isDisplayed(task.inpDate)
        webdriver.isDisplayed(task.inpTime)
        webdriver.isDisplayed(task.btnCancel)
        webdriver.isDisplayed(task.btnSave)

    # 002 - Persistence Cancel Task Component
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

    # 003 - Persistence Save Task Component
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


