from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path="/Users/fdomfeh/Downloads/chromedriver")
        print("Launching Chrome browser......")
    elif browser == "firefox":
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(executable_path="/Users/fdomfeh/WorkSpace/hosted-payment-page-tests/drivers/geckodriver")
        print("Launching Firefox browser.......")
    elif browser == 'Opera':
        driver = webdriver.Opera()
        print("Launching Opera browser.......")
    else:
        driver = webdriver.Safari()
        print("Launching Safari browser......")
    return driver


# This will get the value from CLI /hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

# This will return the Browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############### Generate PyTest HTML Report ################
# It is hooks for Adding Environment info to HTML Report
# To access the metadata from a plugin, you can use the _metadata attribute of the config object
# This can be used to read/add/modify the metadata:

def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'nop commerce'
        config._metadata['Module Name'] = 'Customer'
        config._metadata['Tester'] = 'Frankie'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
