*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem

*** Variables ***
${BROWSER}        headlesschrome
${URL}            https://www.google.com

*** Test Cases ***
Open Website and Verify Title
    Open Browser    ${URL}    browser=${BROWSER}    
    Maximize Browser Window
    Capture Page Screenshot
    Title Should Be    Google Boss
    Close Browser

*** Keywords ***
Capture Page Screenshot
    [Documentation]    Captures a screenshot of the current page
    Capture Page Screenshot

Maximize Browser Window
    [Documentation]    Maximizes the current browser window
    Maximize Browser Window