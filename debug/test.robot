*** Settings ***
Library        Collections
Library        OperatingSystem
Library        String
Library        XML
Library        SeleniumLibrary  implicit_wait=${IMPLICIT_WAIT}  timeout=${TIMEOUT}

Suite Setup     Open Test Browser Chrome    https://www.google.com       

*** Variables ***
${BROWSER}          headlesschrome
${SELENIUM_SPEED}   0
${DEBUG}            ${false}
${CHROME_BINARY}    ${empty}
${ORG}              ${empty}
${IMPLICIT_WAIT}    7.0
${INITIAL_TIMEOUT}  180.0
${TIMEOUT}          30.0
${LOCATION STRATEGIES INITIALIZED}  ${False}
${DEFAULT BROWSER SIZE}  1280x1024

*** Keywords ***
Open Test Browser Chrome
    [Documentation]  Opens a Chrome browser window and navigates to the org
    ...  This keyword isn't normally called directly by a test. It is used
    ...  by the `Open Test Browser` keyword.

    [Arguments]     ${login_url}  ${alias}=${NONE}
    ${options} =                Get Chrome Options
    Create Webdriver            Chrome  options=${options}  alias=${alias}
    Set Selenium Implicit Wait  ${IMPLICIT_WAIT}
    Set Selenium Timeout        ${TIMEOUT}
    Go To                       ${login_url}

Get Chrome Options
    [Documentation]
    ...  Returns a dictionary of chrome options, for use by the keyword `Open Test Browser`.
    ...
    ...  This keyword is not intended to be used by test scripts.
    ${options} =    Evaluate  selenium.webdriver.ChromeOptions()  modules=selenium
    Run Keyword If  '${BROWSER}' == 'headlesschrome'
    ...             Chrome Set Headless  ${options}
    Run Keyword If  '${CHROME_BINARY}' != '${empty}'
    ...             Chrome Set Binary  ${options}
    Call Method  ${options}  add_argument  --disable-notifications
    [return]  ${options}

Chrome Set Binary
    [Documentation]
    ...  Sets the 'options.binary_location' value in the chrome options dictionary
    ...  to the value of the environment variable CHROME_BINARY, if set.
    ...
    ...  This keyword is not intended to be used by test scripts

    [Arguments]  ${options}
    ${options.binary_location} =  Set Variable  ${CHROME_BINARY}
    [return]  ${options}

Chrome Set Headless
    [Documentation]
    ...  This keyword is used to set the chrome options dictionary values
    ...  required to run headless chrome.
    ...
    ...  This keyword is not intended to be used by test scripts

    [Arguments]  ${options}
    Call Method  ${options}  set_headless  ${true}
    Call Method  ${options}  add_argument  --disable-dev-shm-usage
    Call Method  ${options}  add_argument  --disable-background-timer-throttling
    [return]  ${options}

*** Test Cases ***
Open Website and Verify Title
    Title Should Be    Google Boss
    Close Browser