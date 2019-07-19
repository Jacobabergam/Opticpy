rem @echo off
rem This batch file provides a 
rem way to check if virtual env exists 
rem update the virtual env if it does
rem or create and populate with requiremets.txt
rem then it open virtual env for Windows.
rem To run type ".\Update.bat"

IF /I %1 == install     goto :install
IF /I %1 == activate    goto :activate
IF /I %1 == update      goto :update
IF /I %1 == save        goto :save

:install
    virtualenv .env
    .\.env\Scripts\activate.bat
    pip install -r requirements.txt
goto EOF

:activate
IF EXIST ".env" (
    .\.env\Scripts\activate
)
goto EOF

:update
IF EXIST ".env\" (
    pip install -r requirements.txt -q
)

:save
    pip freeze freeze > requirements.txt
    deactivate
goto EOF