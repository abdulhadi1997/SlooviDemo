import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LogInModule
import src.domain.modules.taskModule as TaskModule

from src.domain.unitTest import Test


# 001 - Initial Presentation
class InitialPresentation(Test):

    def setUp(self):
        webdriver = WebDriver.WebDriver(self.driver)
        logIn = LogInModule.LoginPage(self.driver)
        task = TaskModule.TaskModule(self.driver)

        logIn.logIn()
        webdriver.driver.get('https://stage.outreach.sloovi.com/lead/lead_7e0ce02cc9854ceeb61ea58bbae3f2b6')
        webdriver.waitForElementToAppear(task.lblComponentHeader)
        webdriver.getElementbyXPath(task.btnAddTask).click()

    def tearDown(self): self.driver.quit()

    def runTest(self):
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




