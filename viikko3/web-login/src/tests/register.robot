*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  jussi
    Set Password  jussi123
    Set Password Confirmation  jussi123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kari1234
    Set Password Confirmation  kari1234
    Submit Registration
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  kari
    Set Password  123
    Set Password Confirmation  123
    Submit Registration
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  kari
    Set Password  oleniloinen
    Set Password Confirmation  oleniloinen
    Submit Registration
    Register Should Fail With Message  Password should contain numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  jari
    Set Password  jari1234
    Set Password Confirmation  jari12345
    Submit Registration
    Register Should Fail With Message  Passwords are different

Register With Username That Is Already In Use
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Registration
    Register Should Fail With Message  User with username ville already exists

Login After Successful Registration
    Set Username  kussi
    Set Password  kussi123
    Set Password Confirmation  kussi123
    Submit Registration
    Registration Should Succeed
    Click Link  Continue to main page
    Main Page Should Succeed
    Logout Main Page
    Set Username  kussi
    Set Password  kussi123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  sari
    Set Password  123
    Set Password Confirmation  123
    Submit Registration
    Register Should Fail With Message  Password too short
    Click Link  Login
    Set Username  sari
    Set Password  123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  ville  ville123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Registration
    Click Button  Register

Submit Credentials
    Click Button  Login

Logout Main Page
    Click Button  Logout

Registration Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Main Page Should Succeed
    Title Should Be  Ohtu Application main page

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}