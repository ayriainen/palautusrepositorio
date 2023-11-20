*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pasi
    Set Password  Pasi123!
    Set Password Confirmation  Pasi123!
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  p
    Set Password  Pasi123!
    Set Password Confirmation  Pasi123!
    Submit Registration
    Registration Should Fail With Message  Wrong username input

Register With Valid Username And Invalid Password
    Set Username  besi
    Set Password  p
    Set Password Confirmation  p
    Submit Registration
    Registration Should Fail With Message  Password must be longer than 7 and not just contain letters

Register With Nonmatching Password And Password Confirmation
    Set Username  bosi
    Set Password  Pasi123!
    Set Password Confirmation  Pasi123
    Submit Registration
    Registration Should Fail With Message  Passwords must match

Login After Successful Registration
    Set Username  posi
    Set Password  Posi123!
    Set Password Confirmation  Posi123!
    Submit Registration
    Registration Should Succeed
    Go To Login Page
    Login Page Should Be Open
    Set Username  posi
    Set Password  Posi12!
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  p
    Set Password  Pasi123!
    Set Password Confirmation  Pasi123!
    Submit Registration
    Registration Should Fail With Message  Wrong username input
    Go To Login Page
    Login Page Should Be Open
    Set Username  p
    Set Password  Pasi123!
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}