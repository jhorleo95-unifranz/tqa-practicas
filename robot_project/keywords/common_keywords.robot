*** Settings ***
Library    SeleniumLibrary
Resource   ../variables/common_variables.robot

*** Keywords ***
Abrir Navegador Y Maximizar
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10 seconds

Cerrar Navegador
    Close Browser

Navegar A Pagina De Login
    Click Element    xpath=//a[contains(text(), 'Signup / Login')]
    Wait Until Element Is Visible    css=[data-qa='login-email']    10s