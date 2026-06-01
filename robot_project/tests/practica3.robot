*** Settings ***
Documentation    Práctica 3 - Robot Framework (Ejercicios 1, 2 y 3)
Library          SeleniumLibrary
Resource         ../keywords/common_keywords.robot
Resource         ../variables/common_variables.robot

Test Setup       Abrir Navegador Y Maximizar
Test Teardown    Cerrar Navegador

*** Test Cases ***
Ejercicio 1 - Login Correcto
    [Documentation]    Verifica el inicio de sesión con credenciales válidas.
    Navegar A Pagina De Login
    Input Text       css=[data-qa='login-email']       ${VALID_EMAIL}
    Input Text       css=[data-qa='login-password']    ${VALID_PASSWORD}
    Click Element    css=[data-qa='login-button']

    # Validaciones (2 Mínimo)
    Element Should Be Visible    xpath=//a[contains(text(), 'Logged in as')]
    Page Should Contain          Logged in as

    # Captura de pantalla (Se guarda en la carpeta screenshots)
    Capture Page Screenshot      ${EXECDIR}/screenshots/ejercicio1_login_correcto.png

Ejercicio 2 - Login Incorrecto
    [Documentation]    Verifica que el sistema muestre error con credenciales inválidas.
    Navegar A Pagina De Login
    Input Text       css=[data-qa='login-email']       ${INVALID_EMAIL}
    Input Text       css=[data-qa='login-password']    ${INVALID_PASSWORD}
    Click Element    css=[data-qa='login-button']

    # Validaciones (2 Mínimo)
    Element Should Be Visible    xpath=//p[contains(text(), 'Your email or password is incorrect!')]
    Page Should Contain          Your email or password is incorrect!

    # Captura de pantalla
    Capture Page Screenshot      ${EXECDIR}/screenshots/ejercicio2_login_incorrecto.png

Ejercicio 3 - Busqueda De Productos
    [Documentation]    Verifica la búsqueda de productos en el catálogo.
    Click Element                    xpath=//a[contains(text(), 'Products')]
    Wait Until Element Is Visible    id=search_product    10s
    Input Text                       id=search_product    ${SEARCH_TERM}
    Click Element                    id=submit_search

    # Validaciones (2 Mínimo)
    Wait Until Page Contains     Searched Products    10s
    Element Should Be Visible    css=h2.title.text-center

    # Captura de pantalla
    Capture Page Screenshot      ${EXECDIR}/screenshots/ejercicio3_busqueda_productos.png