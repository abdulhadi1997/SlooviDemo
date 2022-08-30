import config.webdriver as WebDriver


class TaskModule:

    btnAddTask = '//button[@data-testid="add-task"]'
    lblTaskDescription = '//*[@for=":r1:"]/span'
    lblFirstTaskComponent = '(//div[@class="Task__description"])[1]'
    inpTaskDescription = '//input[@id=":r1:"]'
    lblDate = '//label[@for=":r0:"]'
    inpDate = '//input[@name="task_date"]'
    inpTime = '//input[@name="task_time"]'
    lblComponentHeader = '//h2[text()="Tasks"]'
    lblAssignUser = '//span[text()="Assign User"]'
    edpAssignUser = '//input[@id="assigned_user"]'
    btnCancel = '//button[@class="btn btn-link cancel-edit"]'
    btnSave = '//button[@class="btn btn-primary"]'

    def __init__(self, driver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver

    def setTaskDescription(self, taskDescription):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.inpTaskDescription).send_keys(taskDescription)

    def setDate(self, date):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.inpDate).send_keys(date)

    def setTime(self, time):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.inpTime).send_keys(time)

    def setAssignUser(self, user):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.edpAssignUser).send_keys(user)
