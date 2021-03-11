*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  harri
    Set Password  harri123
    Set Password Confirmation  harri123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ha
    Set Password  harri123
    Set Password Confirmation  harri123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  masa123
    Set Password Confirmation  masa123
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  matti
    Set Password  matti123
    Set Password Confirmation  matti1234
    Submit Credentials
    Register Should Fail With Message  Password confirmation failed

Login After Successful Registration
    Set Username  pertti
    Set Password  pertti123
    Set Password Confirmation  pertti123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  pertti
    Set Password  pertti123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username  uolevi
    Set Password  uolevi123
    Set Password Confirmation  uolevi1234
    Submit Credentials
    Register Should Fail With Message  Password confirmation failed
    Go To Login Page
    Set Username  uolevi
    Set Password  uolevi123
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
