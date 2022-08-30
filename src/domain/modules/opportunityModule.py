import config.webdriver as WebDriver


class OpportunityModule:
    btnAddOpportunity = '//div[contains(@class,"Opportunities")]//*[@data-testid="add-undefined"]'
    btnCancel = '//button[@class="Button btn btn-link"]'
    btnSave = '//button[@class="Button btn btn-primary"]'
    lblOpportunityHeader = '//div[contains(@class,"Opportunities")]//h2'
    lblStatus = '//span[text()="Status"]'
    inpStatus = '//div[@class="OpportunityEditForm_status"]//input'
    lblEstimatedClose = '//span[text()="Estimated Close"]'
    inpEstimatedClose = '//div[@class="OpportunityEditForm_shrinkItem"]//div[@class="InputField__fieldContainer"]//input'
    lblConfidence = '//span[@class="RangeInput_FormikRangeInput_label_1e0"]'
    valueConfidence = '//span[@class="RangeInput_FormikRangeInput_perc_845"]'
    scrollerConfidence = '//input[@name="confidence"]'
    lblValue = '//span[text()="Value"]'
    inpValue = '//input[@name="value"]'
    edpValue = '//div[@class="EditForm_valuePeriod__iTfOV"]//input[@type="search"]'
    lblContact = '//span[text()="Contact"]'
    edpContact = '//div[@class="InputField InputField--small"]//input[@placeholder="None"]'
    lblUser = '//span[text()="User"]'
    inpUser = '(//div[@class="InputField InputField--small"]//input[@type="search"])[2]'
    lblNotes = '//label[@for="msg"]/span'
    inpNote = '//textarea[@id="msg"]'

    lblStatusListName = '//small[@class="Select__selectedGroup"]'
    lblStatusSubListName = '//div[@class="OpportunityEditForm_status"]//span[@class="Select__selectedText"]'

    btnListOptionBoost = '//div[text()="boost"]/following-sibling::span'
    btnListOptionBaddo = '//div[text()="baddo"]/following-sibling::span'
    btnListOptionSales = '//div[text()="Sales"]/following-sibling::span'

    subListOptionBads = '//div[text()="bads"]'
    subListOptionName = '//div[text()="name"]'
    subListoptionDemoCompleted = '//div[text()="Demo Completed"]'

    lblOpportunityName = '//div[@class="Opportunity__name"]'
    lblOpportunityDate = '//div[@class="Opportunity__confidenceAndDate"]'
    lblOpportunityStatus = '//span[@class="Opportunity__statusText"]'
    lblOpportunityNote = '//div[@class="Opportunity__detail"]'
    lblOpportunityContact = '//div[@class="Opportunity__contactName"]'

    def __init__(self, driver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver

    def resetStatusComponent(self):
        webdriver = WebDriver.WebDriver(self.driver)

        if webdriver.isDisplayed(self.subListOptionBads):
            webdriver.getElementbyXPath(self.btnListOptionBoost).click()

        if webdriver.isDisplayed(self.subListOptionName):
            webdriver.getElementbyXPath(self.btnListOptionBaddo).click()

        if webdriver.isDisplayed(self.subListoptionDemoCompleted):
            webdriver.getElementbyXPath(self.btnListOptionSales).click()

    def setConfidence(self, confidence):
        webdriver = WebDriver.WebDriver(self.driver)

        slider = webdriver.getElementbyXPath(self.scrollerConfidence)
        # self.driver.execute_script("arguments[0].setAttribute('value','" + confidence + "')", slider)

    def setStatus(self, listOption, subListOption):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.inpStatus).click()
        self.resetStatusComponent()

        webdriver.getElementbyXPath('//div[text()="' + listOption + '"]/following-sibling::span').click()
        webdriver.getElementbyXPath('//div[text()="' + subListOption + '"]').click()

        webdriver.waitForElementToHaveText(self.lblStatusListName, listOption.upper())
        webdriver.waitForElementToHaveText(self.lblStatusSubListName, subListOption)

    def setEstimatedClose(self, date):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.inpEstimatedClose).send_keys(date)

    def setValue(self, amount, duration):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.inpValue).clear()
        webdriver.getElementbyXPath(self.inpValue).send_keys(amount)
        webdriver.getElementbyXPath(self.edpValue).send_keys(duration)

    def setContact(self, contact):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.edpContact).send_keys(contact)

    def setUser(self, user):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.inpUser).send_keys(user)

    def setNote(self, note):
        webdriver = WebDriver.WebDriver(self.driver)
        webdriver.getElementbyXPath(self.inpNote).send_keys(note)
