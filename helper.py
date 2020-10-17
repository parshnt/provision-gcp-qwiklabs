# a place to place all the helper funcitions :)
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = 'https://console.cloud.google.com/'

# BROWSER OPTIONS TO AID IN AUTOMATION
op = Options()

op.add_argument("start-maximized")

op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option(
    "prefs",
    {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
    },
)


# SELENIUM FUNCTIONS
class webDriver:

    # START BROWSER WITH OP()
    def __init__(self):
        self.driver = webdriver.Chrome(options=op)

    # LOGIN INTO G-ACCOUNT
    def googleLogin(self, userid, passwd):

        driver = self.driver

        driver.get(
            "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https://developers.google.com/oauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow"
        )

        sleep(3)

        try:

            try:
                driver.find_element_by_name("identifier").send_keys(userid)
                sleep(1)
            except:
                driver.find_element_by_name("Email").send_keys(userid)
                sleep(1)
            try:
                driver.find_element_by_id("identifierNext").click()
                sleep(4)
            except:
                driver.find_element_by_id("next").click()
                sleep(4)
            try:
                driver.find_element_by_name("password").send_keys(passwd)
                sleep(1)
            except:
                driver.find_element_by_name("Passwd").send_keys(passwd)
                sleep(1)
            try:
                driver.find_element_by_id("passwordNext").click()
                sleep(4)
            except:
                driver.find_element_by_id("trustDevice").click()
                driver.find_element_by_id("submit").click()
                sleep(4)
            try:
                driver.find_element_by_id("accept").click()
            except:
                sleep(2)
                driver.find_element_by_id("accept").click()
        except Exception as e:

            print("\nLogin failed, please open an issue on GitHub")
            print(e)

    # NAVIGATE TO G-CLOUD CONSOLE & ACCEPT TnC
    def openConsole(self):

        driver = self.driver

        driver.get(BASE_URL)

        driver.implicitly_wait(5)

        try:

            checkBox = driver.find_element_by_xpath("//*[@id='mat-checkbox-2']/label/div")
            checkBox.click()

            sleep(1)

            dropDown = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/mat-dialog-container/xap-deferred-loader-outlet/ng-component/mat-dialog-content/form/cfc-tos-checkboxes/form/div[1]/cfc-loader/div/mat-form-field")
            dropDown.click()

            countryButton = driver.find_elements_by_xpath("//*[contains(text(), 'India')]")
            countryButton[1].click()

            sleep(1)

            agreeButton = driver.find_elements_by_xpath("//*[contains(text(), 'Agree and continue')]")
            agreeButton[0].click()

        except Exception as e:

            print("\nSomething broke in openConsole(). Please open an issue on GitHub")
            print(e)
            return False

    # NAVIGATE TO PROJECT URL AFTER ACCEPTING TnC
    def openProject(self,id):
        self.driver.get(BASE_URL + "getting-started?project=" + id)

    # CLOSE BROWSER SESSION
    def closeBrowser(self):
        self.driver.quit()
        print("\nBrowser closed!")



## END-OF-FILE ##
