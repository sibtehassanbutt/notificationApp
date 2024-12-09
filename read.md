After making any change in the script i.e. notification_app .py

use the below command to make the app:

pyinstaller --onefile --icon=icon.ico --add-data "icon.ico;." --hidden-import plyer.platforms.win.notification notification_app.py

step one open the folder "D:\python\app_testing\hourly_notifcation\dist"

1. use git bash to open in terminal
2. run pyinstaller --onefile --icon=icon.ico --add-data "icon.ico;." --hidden-import plyer.platforms.win.notification notification_app.py

3. cd dist/
4. ./notification_app [run]
5. test


******
Admin@Office MINGW64 /d/python/app_testing/hourly_notifcation (master)
$ ls
__pycache__/  dist/          icon.ico             notification_app.spec
build/        hook-plyer.py  notification_app.py  requirements.txt
*****
