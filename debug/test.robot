*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem

*** Variables ***
${BROWSER}        headlesschrome
${URL}            https://www.google.com

*** Test Cases ***
Open Website and Verify Title
    Open Browser    ${URL}    browser=${BROWSER}    
    Title Should Be    Google Boss
    Close Browser