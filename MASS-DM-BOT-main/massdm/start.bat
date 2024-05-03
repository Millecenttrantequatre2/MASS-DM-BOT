@echo off
color 3
echo Bonjour et bienvenue dans le script MassDm fait par 1134.
set /p answer="Veux-tu continuer? (Y/N)? "
if /i "%answer%"=="Y" (
  echo You chose to continue.
  python massdm.py
) else if /i "%answer%"=="N" (
  echo You chose to cancel.
  timeout /t 0.5 /nobreak
  exit
) else (
  echo Invalid input.
  timeout /t 5 /nobreak
  exit
)
echo Appuie sur n'importe quelle touche pour quitter...
pause > nul