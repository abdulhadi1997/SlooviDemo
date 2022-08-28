import unittest

import src.domain.webdriver as WebDriver
import src.domain.modules.loginModule as LogInModule
import src.domain.modules.taskModule as TaskModule

from src.domain.unitTest import Test


# 002 - Persistence Cancel Task Component
class PersistenceCancelTask(Test):

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
        taskDescription = Test.randomizeName(self.driver, 'persistenceCancelTest')

        webdriver.clearField(task.inpTaskDescription, 8)
        task.setTaskDescription(taskDescription)
        task.setDate('09/30/2022')
        task.setTime('01:00am')
        task.setAssignUser('Saravanan C')
        webdriver.getElementbyXPath(task.btnCancel).click()
        webdriver.waitForElementToDisappear(task.lblTaskDescription)
        assert webdriver.getElementText(task.lblFirstTaskComponent) != taskDescription






