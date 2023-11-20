*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pasi  Pasi1234!
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  p  Pasi1234!
    Output Should Contain  Wrong input

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  Pasi1234!  Pasi1234!
    Output Should Contain  Wrong input

Register With Valid Username And Too Short Password
    Input Credentials  pasi  Pasi12!
    Output Should Contain  Password must be longer than 7 and not just contain letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pasi  pasipasipasi
    Output Should Contain  Password must be longer than 7 and not just contain letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command